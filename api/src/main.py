from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from map import get_map
from validator import validate_params

app = FastAPI()


@app.get("/map/")
async def map_root(rect: str, width: int = 800, param: str = 'pm25', date: str = 'latest', segments_x: int = 8):
    """
    Main endpoint for producing a map
    :param rect: list of 4 coordinates enclosing an area to gt data for, separated by commas, e.g. 51,14.5,52,15.5
    :param width: width of the result map in pixels. Height is calculated to maintain the ratio of given coordinates.
        Defaults to 800. The supported range is [100;2560]
    :param param: the air pollution parameter to show on map. One of: 'no2', 'o3', 'pm25', 'so2', 'pm10', 'co', 'c6h6'.
        Defaults to PM2.5
    :param date: Date in format YYYY-MM-DDTHH:00:00, e.g. 2021-04-06T16:00:00. Defaults to 'latest' for the current hour
    :param segments_x: number of segments along the x axis to divide map in. Segments along the y axis are calculated
        proportionally. Defaults to 8
    :return: map as a png file
    """
    if date == 'latest':
        date = datetime.now().strftime("%Y-%m-%dT%H:00:00")

    validate_params(rect, width, param, date, segments_x)

    return StreamingResponse(get_map(rect, width, param, date, segments_x), media_type=f"image/png",
                             headers={'Content-Disposition': f'inline; filename="map.png"'})


@app.get("/")
async def index():
    """
    Endpoint for the root element, redirecting to project repository
    :return: link to project repo
    """
    return {"Api usage as described in https://github.com/MaciejMarkiewicz/air-quality"}