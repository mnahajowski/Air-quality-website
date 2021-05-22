import requests
import io
import os
import yaml
from PIL import Image, ImageDraw

from mask import get_data_form_mask

MAPS_BASE_ENDPOINT = f"https://maps.geoapify.com/v1/staticmap?style=osm-carto&apiKey={os.getenv('MAPS_API_KEY')}"
DARK_RED_COLOR = (135, 0, 0)
GREY_COLOR = (180, 180, 180)
TEXT_COLOR = (0, 0, 0)
TEXT_MARGIN = 5


def get_map(rect, width, param, date, segments_x):
    """
    Gets a map image for chosen parameters
    :param rect: list of 4 coordinates enclosing an area to gt data for, separated by commas
    :param width: width of the result map in pixels
    :param param: the air pollution parameter to show on map. One of: 'no2', 'o3', 'pm25', 'so2', 'pm10', 'co', 'c6h6'.
    :param date: Date in format YYYY-MM-DDTHH:00:00, e.g. 2021-04-06T16:00:00
    :param segments_x: number of segments along the x axis to divide map in.
    :return: a map png file
    """
    lat_1, lon_1, lat_2, lon_2 = [float(val) for val in rect.split(',')]
    height = int(width * (lat_2 - lat_1) // (lon_2 - lon_1))
    segments_y = int(height / width * segments_x)

    map = _get_raw_map(f"{lon_1},{lat_1},{lon_2},{lat_2}", width, height)
    mask = _get_mask(width, height, segments_x, segments_y, rect, date, param)

    try:
        combined = Image.blend(map, mask, 0.5)
    except Exception as e:
        print(e, map, mask)
        res = io.BytesIO()
        res.seek(0)
        return res

    stream = io.BytesIO()
    combined.save(stream, format='png')
    stream.seek(0)

    return stream


def _get_raw_map(rect, width, height):
    """
    Gets a raw map from the map api
    :param rect: list of 4 coordinates enclosing an area to gt data for, separated by commas
    :param width: width of the result map in pixels
    :param height: height of the result map in pixels
    :return: raw map image
    """
    url = MAPS_BASE_ENDPOINT + f"&area=rect:{rect}&width={width}&height={height}&format=png"
    res = requests.get(url)

    return Image.open(io.BytesIO(res.content)).convert('RGBA')


def _get_mask(width, height, segments_x, segments_y, rect, date, param):
    """
    Gets a map mask containing the air quality data
    :param width: width of the mask in pixels
    :param height: height of the mask in pixels
    :param segments_x: number of segments along the x axis to divide map in.
    :param segments_y: number of segments along the y axis to divide map in.
    :param rect: list of 4 coordinates enclosing an area to gt data for, separated by commas
    :param date: Date in format YYYY-MM-DDTHH:00:00, e.g. 2021-04-06T16:00:00
    :param param: the air pollution parameter to show on map. One of: 'no2', 'o3', 'pm25', 'so2', 'pm10', 'co', 'c6h6'.
    :return: mask image
    """
    segments = get_data_form_mask(segments_x, segments_y, rect, date, param)

    with open(os.path.join(os.path.dirname(__file__), 'color_config.yaml')) as f:
        color_data = yaml.safe_load(f)

    config = color_data[param]
    offsets_x, offsets_y = _get_image_offsets(width, height, segments_x, segments_y)
    mask = Image.new('RGBA', (width, height))

    for idx_row, row in enumerate(segments):
        for idx_col, segment in enumerate(row):
            img = Image.new('RGBA', (offsets_x[idx_col + 1] - offsets_x[idx_col], offsets_y[idx_row + 1] -
                                     offsets_y[idx_row]), (*_get_color_for_value(segment, config), 150))
            draw = ImageDraw.Draw(img)
            text = f"{segment:.1f}" if segment is not None else 'no data'
            draw.rectangle((0, 0, len(text) * 6 + 10, 20), fill='white')
            draw.text((TEXT_MARGIN, TEXT_MARGIN), text, TEXT_COLOR)

            mask.paste(img, (offsets_x[idx_col], offsets_y[idx_row]))

    return mask


def _get_image_offsets(width, height, segments_x, segments_y):
    """
    Gets offsets for the segments
    :param width: map width
    :param height: map height
    :param segments_x: number of x segments
    :param segments_y: number of y segments
    :return: lists of x offsets, lists of y offsets
    """
    offsets_x = []
    offsets_y = []

    for i in range(segments_x):
        offsets_x.append((int(width / segments_x * i)))
    for i in range(segments_y):
        offsets_y.append((int(height / segments_y * i)))

    offsets_x.append(width)
    offsets_y.append(height)

    return offsets_x, offsets_y


def _get_color_for_value(value, config):
    """
    Gets color for the current value from the config
    :param value: parameter value
    :param config: color config
    :return: color code
    """
    for threshold, color in config.items():
        if value is None:
            return GREY_COLOR
        if threshold >= value:
            return color

    return DARK_RED_COLOR
