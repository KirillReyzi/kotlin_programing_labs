from XmlReader import Xml
from CsvReader import Csv
from AbstractReadable import Readable
import time


class TimeChecker:
    def __init__(self):
        self.__reader = Readable

    def start_processing(self, path: str):
        timer = time.time()

        if self.__read_file(path):
            print(f"\nВремя потраченное на чтение - {time.time() - timer}\n")
            prev = time.time() - timer
            self.__reader.find_duplicate()
            print(f"\nВремя потраченное на подсчет дубликатов - {time.time() - timer - prev}\n")
            prev = time.time() - timer
            self.__reader.counting_builds()
            print(f"\nВремя потраченное на подсчет зданий - {time.time() - timer - prev}\n")
            print(f"Общее время на обработку - {time.time() - timer}\n")
            return
        print("Неверный путь к файлу или неверный формат!!!")

    def __read_file(self, path):
        if len(path) <= 3:
            return False

        if path[-3:] == "xml":
            self.__reader = Xml()

        elif path[-3:] == "csv":
            self.__reader = Csv()
        else:
            return False

        return self.__reader.read(path)


def loop():
    data = TimeChecker()
    while True:
        print("Введите 'exit' для завершения")
        print("Введите путь к файлу")
        path = str(input())
        if path == "exit":
            break
        data.start_processing(path)


if __name__ == '__main__':
    loop()
