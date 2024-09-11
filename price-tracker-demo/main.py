"""
Price tracker CLI app

- Add a page to track (URL/name)
- List all tracked items and their current price
- (Nice to have) Show history for an item
"""
from typing import List

from cli import load_cli
from item import Item
from scraper import get_price
from state import save_state, load_state

def add_to_list(url: str, items: List[Item]):
    price = get_price(url)

    item = Item(url, url, price)

    items.append(item)


if __name__ == "__main__":
    args = load_cli()

    items = load_state()

    if args.item_url is not None:
        # Add new item
        add_to_list(args.item_url, items)
    else:
        # List
        for item in items:
            print(item)

    save_state(items)
