import abc
import csv
import os.path
from typing import List

from happybirthday.columns import Column


class GreetingStore(abc.ABC):
    @abc.abstractmethod
    def import_columns(self) -> List[Column]:
        raise NotImplementedError()


class GreetingStoreCSV(GreetingStore):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def import_columns(self) -> List[Column]:
        columns = []
        filename = os.path.join("csv", self.filename)
        with open(filename, newline="") as f:
            columnreader = csv.reader(f, delimiter=";", quotechar="|")
            for row in columnreader:
                cols = list(row)
                columns.append(Column(prefix=cols[0], lines=cols[1:]))
        return columns
