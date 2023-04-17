import json

import requests
from lxml import html

citymap = {}

week_container = []
data_container = []
weather_container = []

def init_citymap():
    file_path = 'citycode.json'
    json_data = json.load(open(file_path, 'r', encoding='utf-8'))
    # 读取文件是否成功
    if not json_data:
        print('读取文件失败')
        return False
    # 遍历json文件 读取城市名和城市代码
    for i in range(len(json_data)):
        city_name = json_data[i]['city_name']
        city_code = json_data[i]['city_code']
        if city_code != '':
            citymap[city_name] = city_code

    return True


def get_citycode(city_name):
    if init_citymap():
        citycode = citymap.get(city_name)
        if citycode:
            return citycode
        else:
            return ''
    return ''


def get_weather_info(cityname):
    citycode = get_citycode(cityname)
    url = 'http://t.weather.itboy.net/api/weather/city/' + citycode
    response = requests.get(url)
    response.encoding = 'utf-8'
    html.fromstring(response.text)
    json_dict = response.json()
    if isinstance(json_dict, dict):
        data_dict = json_dict
    else:
        data_dict = json.loads(json_dict)
    return data_dict

def init_container():
    data = get_weather_info('上海')
    forecast_data = data['data']['forecast']
    for i, day in enumerate(forecast_data):
        if i == 6:
            break
        week_container.append(day["week"])  # 日期
        date = day['ymd']
        date = date.split('-')[1] + '-' + date.split('-')[2]
        data_container.append(date)  # 星期

        weather_container.append(day["type"])  # 天气

if __name__ == '__main__':

    init_container()
    print(citymap)
