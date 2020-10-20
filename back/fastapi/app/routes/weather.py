"""
Created By: S H
Date: 20-10-2020

"""
from fastapi import APIRouter, Response, status
import requests

from .. import config

router = APIRouter()


"""
    weather forcast proxy.
    @param: city the name of the city for which you want forcast data
"""
@router.get('/{city}')
async def get_weather_forcast(city: str, response: Response):
    url = '{}?key={}&q={}&days={}'.format(config.weatherApi, config.apiKey, city, 1)
    data = requests.get(url=url)
    response.status_code = data.status_code
    return data.json()
