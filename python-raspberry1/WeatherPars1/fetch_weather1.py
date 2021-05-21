from requests import get
import json
from pprint import pprint

# https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/
# add weather_stn_id
# https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/1648902

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/1648902'
weather = get(url).json()['items']
pprint(weather)

#
