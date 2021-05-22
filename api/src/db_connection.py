import psycopg2


def select(lat_range, lon_range, date, time):
    """
    Select wrapper for the API
    :param lat_range: latitude range
    :param lon_range: longitude range
    :param date: date to select data for
    :param time: time to select data for
    :return: selected data
    """
    connection = psycopg2.connect(dbname='air_data', user='docker', password='docker', host='dbserver')
    cursor = connection.cursor()

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
