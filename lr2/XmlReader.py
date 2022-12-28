import xml.etree.ElementTree as ElementTree
from AbstractReadable import Readable


class Xml(Readable):
    def read(self, path):
        try:
            tree = ElementTree.parse(path)
            for row in tree.getroot():
                self._file.append(row.attrib)
        except FileNotFoundError:
            return False
        return True
