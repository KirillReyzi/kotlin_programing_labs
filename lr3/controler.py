import telebot
from weather import WeatherChecker
from telebot import types


class WeatherBot:
    def __init__(self, path_weather_api_key="weather_api_key", path="telegram_bot_token"):
        self.__token = None
        try:
            self.__token = open(path, "r").read()
        except FileNotFoundError:
            self.__token = None
            print("Неверный путь")
            return
        self.__bot = telebot.TeleBot(self.__token)
        self.__weather_check = WeatherChecker(path_weather_api_key)

        @self.__bot.message_handler(content_types=['text'])
        def start(message):
            self.__keyboard_start(message)

        def weather(message):
            self.__bot.send_message(message.from_user.id, self.__weather_check.check(message.text))
            self.__keyboard_start(message)

        @self.__bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "weather":
                self.__bot.send_message(call.message.chat.id, 'Введите название города.')
                self.__bot.register_next_step_handler(call.message, weather)

    def __keyboard_start(self, message):
        keyboard = types.InlineKeyboardMarkup()
        key_weather = types.InlineKeyboardButton(text='Погода', callback_data='weather')
        keyboard.add(key_weather)
        text = 'Нажми на кнопку'
        self.__bot.send_message(message.from_user.id, text=text, reply_markup=keyboard)

    def start(self):
        if self.__token is None:
            print("Нет токена")
        self.__bot.polling(none_stop=True, interval=0)
