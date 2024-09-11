"""
Persistent state of the list
"""
from typing import List

import json
from item import Item

STATE_FILEPATH = "state.json"


def load_state() -> List[Item]:
    with open(STATE_FILEPATH, "r") as fp:
        items = json.load(fp)

    return [Item.deserialize(item) for item in items]


def save_state(items: List[Item]):
    content = [item.serialize() for item in items]

    with open(STATE_FILEPATH, "w") as fp:
        json.dump(content, fp)
