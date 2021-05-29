from db_connection import select_pollution_data
from datetime import datetime


def get_data_form_mask(segments_x, segments_y, rect, date, param):
    """
    Returns interpolated data for the mask
    :param segments_x: number of x segments
    :param segments_y: number of y segments
    :param rect: rect data for the map
    :param date: date
    :param param: air quality param
    :return: interpolated data for the mask
    """
    lat_1, lon_1, lat_2, lon_2 = [float(val) for val in rect.split(',')]
    segment_x_size = (lon_2 - lon_1) / segments_x
    segment_y_size = (lat_2 - lat_1) / segments_y

    date = datetime.fromisoformat(date)

    date_string = date.strftime("%Y.%m.%d")
    time_string = date.strftime("%H:%M:%S")

    data = select_pollution_data((lat_1 - 3 * segment_x_size, lat_2 + 3 * segment_x_size),
                                 (lon_1 - 3 * segment_y_size, lon_2 + 3 * segment_y_size),
                                 date_string, time_string)

    return idw(data, param, segments_x, segments_y, lat_1, lon_1, segment_x_size, segment_y_size)


def idw(data, param, num_x, num_y, zero_lat, zero_lon, segment_x_size, segment_y_size):
    """
    IDW algorithm
    :param data: date
    :param param: air quality parameter
    :param num_x: number of x segments
    :param num_y: number of y segments
    :param zero_lat: starting latitude
    :param zero_lon: starting longitude
    :param segment_x_size: size of x segment
    :param segment_y_size: size of y segment
    :return: interpolated data
    """
    result = [[[] for _ in range(num_x)] for _ in range(num_y)]

    for record in data:
        tile_index_x = int((record['lon'] - zero_lon) // segment_x_size)
        tile_index_y = int((record['lat'] - zero_lat) // segment_y_size)

        if 0 <= tile_index_x < num_x and 0 <= tile_index_y < num_y and record[param] is not None:
            result[tile_index_y][tile_index_x].append(record[param])

    for row in result:
        for index, tile in enumerate(row):
            if tile:
                value = sum(tile) / len(tile)
            else:
                value = 0

            row[index] = value

    for index_row, row in enumerate(result):
        for index_col, tile in enumerate(row):
            if not tile:
                row[index_col] = _compute_value(data, (zero_lat + (segment_y_size * (index_row + 0.5))),
                                                (zero_lon + (segment_x_size * (index_col + 0.5))), param,
                                                (segment_x_size + segment_y_size) * 1.5)

    return result


def _compute_value(data, x, y, param, r):
    """
    Computes interpolated value for one segment
    :param data: air data
    :param x: segment x
    :param y: segment y
    :param param: air parameter
    :param r: radius of segments to include
    :return: computed value
    """
    points_with_distances = [(row[param], r - _get_distance(x, y, row['lat'], row['lon'])) for row in data]
    filtered_distances = [pair for pair in points_with_distances if pair[1] > 0 and pair[0] is not None]

    if filtered_distances:
        return sum(val * weight for val, weight in filtered_distances) / sum(weight for _, weight in filtered_distances)
    else:
        return None


def _get_distance(x1, y1, x2, y2):
    """
    :return: distance between points
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
