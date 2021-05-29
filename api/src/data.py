from db_connection import select_stations, select_stations_data


def get_stations():
    return select_stations()


def get_station_data(id_station, date_from, date_to, param):
    return select_stations_data(id_station, *date_from.split('T'), *date_to.split('T'), param)
