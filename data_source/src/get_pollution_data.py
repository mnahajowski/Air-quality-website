"""
A script to run pollution data download. Usage: python ./get_pollution_data.py
"""
import time
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from dao import insert, select

MAP_URL = 'https://powietrze.gios.gov.pl/pjp/current'


def get_pollution_data():
    """
    Runs pollution data download
    :return: a list of records
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(MAP_URL)
    driver.find_element_by_id('panel_sound_btn').click()
    time.sleep(10)

    weather_data = []
    soup = BeautifulSoup(driver.page_source, "html.parser")
    all_stations_data = soup.find(True, {'id': 'panel_sound'})
    station_names = all_stations_data.find_all('div', {'class': 'h3'})
    weather_data_info = soup.find('small').text.split()

    for station_index, station in enumerate(all_stations_data.find_all('ul')):
        station_content = {'date': None, 'hour': None, 'NO2': None, 'O3': None, 'PM2.5': None, 'SO2': None,
                           'PM10': None, 'CO': None, 'C6H6': None}

        for idx, element in enumerate(station.find_all('li')):
            if idx > 0:
                station_content['date'] = weather_data_info[0]

                station_content['hour'] = datetime.strftime(datetime.strptime(weather_data_info[-2], '%H:%M'),
                                                            '%H:%M:%S')
                station_elements = element.text.rpartition(': ')
                station_content['name'] = station_names[station_index].text
                station_content[station_elements[0]] = station_elements[2].rpartition(' ')[0].replace(',', '.')

        weather_data.append(station_content)

    return weather_data


def join_name_with_id(stations, data):
    """
    Performs a join on stations and pollution data
    :param stations: list of stations data for a specific date
    :param data: pollution data
    :return: list of joined data
    """
    mapping = {name.lower().strip(): id_station for id_station, name in stations}

    data = [{'id_station': mapping[row['name'].lower().strip()], **row} for row in data
            if row['name'].lower().strip() in mapping]

    for row in data:
        del row['name']

    return data


def main():
    """
    Runs pollution data download and inserts it to the database
    """
    pollution_data = get_pollution_data()
    date = pollution_data[0]['date']
    stations = select('stations', ['id_station', 'name'], where=f"date = '{date}'")
    insert('pollution', join_name_with_id(stations, pollution_data), columns=['id_station', 'measurement_date',
                                                                              'measurement_time', 'no2', 'o3', 'pm25',
                                                                              'so2', 'pm10', 'co', 'c6h6'])


if __name__ == '__main__':
    main()
