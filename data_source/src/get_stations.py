"""
A script to run stations data download. Usage: python ./get_stations.py
"""
import requests
import json
from datetime import datetime

from dao import insert

STATIONS_API_ENDPOINT = "http://api.gios.gov.pl/pjp-api/rest/station/findAll"


def get_stations():
    """
    Runs stations data download
    :return: a list of records
    """
    res = requests.get(STATIONS_API_ENDPOINT)
    data = json.loads(res.text)
    parsed = [{'id_station': str(record['id']),
               'date': f"{datetime.today().date()}",
               'name': f"{record['city']['name']}, {record['addressStreet'] or ''}",
               'lat': str(record['gegrLat']),
               'lon': str(record['gegrLon'])} for record in data]

    return parsed


def main():
    """
    Gets station data and inserts it to the database
    """
    insert('stations', get_stations())


if __name__ == '__main__':
    main()
