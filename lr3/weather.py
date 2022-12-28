import requests
import json
# icons = ["☀", "🌤", "⛅", "🌥", "☁", "🌧", "🌦", "🌩", "❄", "🌫"]

icons = {"01d": "☀", "01n": "☀",
         "02d": "🌤", "02n": "🌤",
         "03d": "☁", "03n": "☁",
         "04d": "☁", "04n": "☁",
         "09d": "🌧", "09n": "🌧",
         "10d": "🌦", "10n": "🌦",
         "11d": "🌩", "11n": "🌩",
         "13d": "❄", "13n": "❄",
         "50d": "🌫", "50n": "🌫"}


class WeatherChecker:
    def __init__(self, path="weather_api_key"):
        self.__api_key = None
        self.__page_request = None
        self.__page_json = None
        try:
            self.__api_key = open(path, "r").read()
        except FileNotFoundError:
            print("Неверный путь")

    def __request(self, city):
        self.__page_request = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.__api_key}")
        if self.__page_request.status_code != 200:
            return False

        self.__page_json = json.loads(self.__page_request.text)
        return True

    def __to_string(self, city):
        return str(f"{city}: {icons[self.__page_json['weather'][0]['icon']]}\n"
                   f"Температура: {int(self.__page_json['main']['temp'] - 273.15)} °C,\n"
                   f"ощущается как: {int(self.__page_json['main']['feels_like'] - 273.15)} °C.\n"
                   f"Влажность: {self.__page_json['main']['humidity']}%.\n"
                   f"Скорость ветра: {self.__page_json['wind']['speed']} км/ч.\n"
                   )

    def check(self, city):
        if self.__api_key is None:
            return "Нет ключа api!!!"
        if self.__request(city) is False:
            return "Ошибка запроса!!!"
        return self.__to_string(city)
