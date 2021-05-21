from requests import get
import json
from pprint import pprint
from haversine import haversine

# Максимально возможное расстояние между двумя точками на поверхности Земли составляет 20036 км
def find_closest():
    smallest = 20036
    #
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        # определить расстояние до станции
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        # print(distance)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station

#
stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'
# переменные для вашей текущей долготы и широты
my_lat = 52.194504
my_lon = 0.134708
# получить список всех станций
all_stations = get(stations).json()['items']
# id stantion
print(find_closest())

# https://projects.raspberrypi.org/en/projects/fetching-the-weather/9
# Получение данных о погоде
closest_stn = find_closest()
# добавляем ид в урл
weather = weather + str(closest_stn)
#
my_weather = get(weather).json()['items']
pprint(my_weather)
#
