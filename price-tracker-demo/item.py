"""
Class representing an item
"""

import json


class Item:
    def __init__(self, name: str, url: str, price: float = 0.0):
        self.__name = name
        self.__url = url
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name

    @property
    def url(self) -> str:
        return self.__url

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        self.__price = new_price

    def __str__(self) -> str:
        return f'{self.__name}: {self.__price} ({self.__url})'

    def serialize(self) -> str:
        return json.dumps({'name': self.__name, 'url': self.__url, 'price': self.__price})

    @staticmethod
    def deserialize(serialized: str) -> 'Item':
        deserialized = json.loads(serialized)

        return Item(**deserialized)
