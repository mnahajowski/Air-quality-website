import psycopg2


def _connect():
    connection = psycopg2.connect(dbname='air_data', user='docker', password='docker', host='dbserver')
    cursor = connection.cursor()

    return connection, cursor


def select_pollution_data(lat_range, lon_range, date, time):
    """
    Select wrapper for the API
    :param lat_range: latitude range
    :param lon_range: longitude range
    :param date: date to select data for
    :param time: time to select data for
    :return: selected data
    """
    connection, cursor = _connect()

    expression = f"""WITH A as (SELECT id_station, lat, lon FROM stations 
WHERE lat >= {lat_range[0]} AND lat <= {lat_range[1]} AND lon >= {lon_range[0]} AND lon <= {lon_range[1]} 
AND date = '{date}'),
B as (SELECT id_station, no2, o3, pm25, so2, pm10, co, c6h6 FROM pollution
WHERE measurement_date = '{date}' AND measurement_time = '{time}')
SELECT * FROM A 
JOIN B on A.id_station = B.id_station;"""

    cursor.execute(expression)
    data = [{'lat': lat, 'lon': lon, 'no2': no2, 'o3': o3, 'pm25': pm25, 'so2': so2, 'pm10': pm10, 'co': co, 'c6h6': c6h6}
            for _, lat, lon, _, no2, o3, pm25, so2, pm10, co, c6h6 in cursor.fetchall()]

    cursor.close()
    connection.close()

    return data


def select_stations():
    connection, cursor = _connect()

    expression = f"""SELECT DISTINCT id_station, name, lat, lon
                     FROM stations"""

    cursor.execute(expression)
    data = [{"id": id_station, 'name': name, 'lat': lat, 'lon': lon}
            for id_station, name, lat, lon in cursor.fetchall()]

    cursor.close()
    connection.close()

    return data


def select_stations_data(id_station, date_from, time_from, date_to, time_to, param):
    connection, cursor = _connect()

    expression = f"""SELECT measurement_date, measurement_time, {param}
                     FROM pollution
                     WHERE id_station = {id_station} AND
                         ((measurement_date = '{date_from}' AND measurement_time >= '{time_from}' AND
                         (measurement_date < '{date_to}' OR (measurement_date = '{date_to}'
                         AND measurement_time < '{time_to}'))) OR 
                         
                         (measurement_date > '{date_from}' AND
                         (measurement_date < '{date_to}' OR (measurement_date = '{date_to}'
                         AND measurement_time < '{time_to}')))) ORDER BY measurement_date, measurement_time"""

    cursor.execute(expression)
    data = [{"date": date, 'time': time, 'value': value}
            for date, time, value in cursor.fetchall()]


    cursor.close()
    connection.close()

    return data
