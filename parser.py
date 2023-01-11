import requests
from bs4 import BeautifulSoup as bs


url = 'https://pogoda.mail.ru/prognoz/moskva/'
response = requests.get(url).text
soup = bs(response, 'html.parser')


def get_weather(teg):
    weather = soup.find('div', class_=teg)
    weather = weather.text.split()
    return weather


def read_weather(data):
    my_list = []
    temp_list = []
    for i in range(len(data)):
        if i % 12 == 0 and i != 0:
            continue
        else:
            temp_list.append(data[i])
            if len(temp_list) == 11:
                my_list.append(temp_list)
                temp_list = []
            if len(my_list) == 5:
                break
    return my_list


def today(data):
    weather_today_str = 'Сегодня '
    for i in range(len(data)):
        if data[i] != '0':
            weather_today_str += data[i] + ' '
        else:
            break
    return weather_today_str


weather_tomorrow = get_weather("day day_index")
data_weather_tomorrow = read_weather(weather_tomorrow)
weather_week = get_weather('days__wrapper')
data_weather_week = read_weather(weather_week)
weather_today = get_weather('information__content__wrapper information__content__wrapper_left')
weather_today = today(weather_today)

