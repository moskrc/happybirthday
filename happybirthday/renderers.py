from string import Template
from typing import Dict


class ColumnRenderer:
    def __init__(self, context: Dict = None) -> None:
        self.context = context or {}

    def render(self, column: "Column") -> str:
        data = " ".join([column.prefix, column.get_random_line()])
        t = Template(data)
        return t.safe_substitute(**self.context)
