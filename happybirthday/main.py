import logging
from typing import Dict

from happybirthday.renderers import ColumnRenderer
from happybirthday.store import GreetingStore, GreetingStoreCSV

logger = logging.getLogger(__name__)


class GreetingMaker:
    def __init__(self, store: GreetingStore) -> None:
        self.columns = store.import_columns()

    def make_greeting(self, context: Dict) -> str:
        renderer = ColumnRenderer(context)
        parts = [c.render_line(renderer) for c in self.columns]
        return " ".join(parts)


if __name__ == "__main__":
    columns_store = GreetingStoreCSV("data.csv")
    gr = GreetingMaker(store=columns_store)
    for _ in range(10):
        print(gr.make_greeting(context={"nawme": "Марина", "today": "Пн"}))
