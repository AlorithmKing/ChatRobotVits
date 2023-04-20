import json

import requests
from lxml import html

citymap = {}

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



def load_weather_icon(type):
    json_data = json.load(open('weathericon.json', 'r', encoding='utf-8'))
    if not json_data:
        print('读取文件失败')
        return False
    for i in range(len(json_data)):
        if json_data[i]['type'] == type:
            return json_data[i]['img_path']

if __name__ == '__main__':

   json_data = get_weather_info('北京')

   print(json_data)
