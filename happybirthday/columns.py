import random
from dataclasses import dataclass
from typing import List


@dataclass
class Column:
    lines: List[str]
    prefix: str = ""

    def get_random_line(self) -> str:
        return random.choice(self.lines)

    def render_line(self, column_renderer: "ColumnRenderer") -> str:
        return column_renderer.render(self)
