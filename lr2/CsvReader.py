import csv
from AbstractReadable import Readable


class Csv(Readable):
    def read(self, path):
        try:
            reader = csv.DictReader(open(path, 'r', encoding='utf-8'), delimiter=';')
            for row in reader:
                self._file.append(row)
        except FileNotFoundError:
            return False
        return True
