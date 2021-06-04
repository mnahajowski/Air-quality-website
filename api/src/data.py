from db_connection import select_stations, select_stations_data
from datetime import datetime, timedelta


def get_stations():
    return select_stations()


def parse_date_and_time(date, time):
    return datetime.strptime(date + time, '%Y-%m-%d%H:%M:%S')


def split_date_and_time(date):
    return {'date': date.strftime('%Y-%m-%d'), 'time': date.strftime('%H:%M:%S')}


def get_station_data(id_station, date_from, date_to, param):
    data = select_stations_data(id_station, *date_from.split('T'), *date_to.split('T'), param)

    base = datetime.strptime(date_from, '%Y-%m-%dT%H:%M:%S')
    end = datetime.strptime(date_to, '%Y-%m-%dT%H:%M:%S')
    expected_dates = [base + timedelta(hours=x) for x in range(int((end - base).total_seconds() / 3600))]

    data = {parse_date_and_time(str(row['date']), str(row['time'])): row['value'] for row in data}
    result = [{**split_date_and_time(date), 'value': data.get(date, 0)} for date in expected_dates]

    return result
