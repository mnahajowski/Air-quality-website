from datetime import datetime
from fastapi import HTTPException


def validate_params(rect: str, width: int, param: str, date: str, segments_x: int):
    """
    Validate map endpoint parameters
    :param rect: rect parameter
    :param width: width parameter
    :param param: air quality param parameter
    :param date: date parameter
    :param segments_x: number of segments parameter
    :return: None
    :raises: HTTPException 404 on wrong data
    """
    try:
        rect = [float(coord) for coord in rect.split(',')]
        if not (0 <= rect[0] <= 90 and 0 <= rect[2] <= 90 and 0 <= rect[1] <= 180 and 0 <= rect[3] <= 180):
            HTTPException(status_code=404, detail="Wrong rect coordinates range")
    except Exception:
        raise HTTPException(status_code=404, detail="Wrong rect coordinates format")

    try:
        width = int(width)
    except ValueError:
        raise HTTPException(status_code=404, detail="Wrong width format")
    else:
        if not 100 <= width <= 2560:
            raise HTTPException(status_code=404, detail="Wrong width range")

    if param not in ('no2', 'o3', 'pm25', 'so2', 'pm10', 'co', 'c6h6'):
        raise HTTPException(status_code=404, detail="Wrong parameter")

    try:
        datetime.strptime(date, "%Y-%m-%dT%H:00:00")
    except Exception:
        raise HTTPException(status_code=404, detail="Wrong date format")

    try:
        segments_x = int(segments_x)
    except ValueError:
        raise HTTPException(status_code=404, detail="Wrong segments_x format")
    else:
        if not 1 <= segments_x <= 20:
            raise HTTPException(status_code=404, detail="Wrong width range")
