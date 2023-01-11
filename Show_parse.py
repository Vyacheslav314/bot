import parser

class Weather:
    def __init__(self, day, temperate_d, temperate_n, sky, pressure, air_humidity,
                 wind_speed, ultraviolet_index, probability_precipitation):
        self.day = day
        self.temperate_d = temperate_d
        self.temperate_n = temperate_n
        self.sky = sky
        self.pressure = pressure
        self.air_humidity = air_humidity
        self.wind_speed = wind_speed
        self.ultraviolet_index = ultraviolet_index
        self.probability_precipitation = probability_precipitation

    def __str__(self):
        return f'День: {self.day}\n' \
               f'Температура днём: {self.temperate_d}\n' \
               f'Температура ночью: {self.temperate_n}\n' \
               f'Небо: {self.sky}\n' \
               f'Давление: {self.pressure}\n' \
               f'Влажность воздуха: {self.air_humidity}\n' \
               f'Скорость ветра: {self.wind_speed}\n' \
               f'Ультрафиолет: {self.ultraviolet_index}\n' \
               f'Вероятность осадков: {self.probability_precipitation}\n' \
               f'********************************\n'


def show_weather(data):
    str_weather = ''
    for i in range(len(data)):
        show = Weather(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]+data[i][5], data[i][6], data[i][7]+data[i][8], data[i][9], data[i][10])
        str_weather += str(show)
    return str_weather
