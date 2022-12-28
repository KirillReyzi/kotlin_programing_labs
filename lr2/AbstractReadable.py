from abc import ABC, abstractmethod


class Readable(ABC):
    def __init__(self):
        self._file = []

    @property
    def file(self):
        return self._file

    @abstractmethod
    def read(self, path):
        """Чтение файла"""

    def find_duplicate(self):
        rows = set()
        dup = dict()
        for row in self._file:
            if str(row) in rows:
                if dup.get(str(row)) is None:
                    dup[str(row)] = 0
                dup[str(row)] += 1
            rows.add(str(row))

        self._print_duplicate(dup)

    def counting_builds(self):
        rows = set()
        builds = dict()
        for row in self._file:
            if str(row) in rows:
                continue
            rows.add(str(row))
            if builds.get(row["city"]) is None:
                builds[row["city"]] = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
            builds[row["city"]][row["floor"]] += 1

        self._print_builds(builds.items())

    @staticmethod
    def _print_duplicate(dup):
        for i in dup.items():
            str_dict = eval(i[0])
            print(f'"{str_dict["city"]}";'
                  f'"{str_dict["street"]}";'
                  f'{str_dict["house"]};'
                  f'{str_dict["floor"]}'
                  f' - duplicate amount : {i[1]}')

    @staticmethod
    def _print_builds(builds):
        for i in builds:
            print(f'{i[0]} :\n'
                  f'Количество этажей\t-\t\t1\t\t2\t\t3\t\t4\t\t5\n'
                  f'Количество домов\t-\t{i[1]["1"]}\t{i[1]["2"]}\t{i[1]["3"]}\t{i[1]["4"]}\t{i[1]["5"]}')
