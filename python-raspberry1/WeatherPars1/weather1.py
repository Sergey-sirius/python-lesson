from requests import get
import json
from pprint import pprint

# Поиск метеостанции
# список всех метеостанций, которые в настоящее время находятся в сети, используя простой URL-адрес
# weather_stn_id- уникальный ID станции ( weather_stn_id)
# его расположение в мире (вы узнаете об этом позже в проекте)
# weather_stn_lat - широта
# weather_stn_long - долгота
# weather_stn_name- название метеостанции.

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
#
stations = get(url).json()['items']
pprint(stations)
#
