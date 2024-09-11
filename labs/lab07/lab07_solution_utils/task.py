import json


class Task:
    def __init__(self, name: str, task_id: int):
        self.__name = name
        self.__id = task_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def task_id(self) -> int:
        return self.__id

    def to_json(self) -> str:
        return json.dumps({'name': self.name, 'task_id': self.task_id})

    @staticmethod
    def from_json(content: str) -> 'Task':
        return Task(**json.loads(content))

    def __str__(self) -> str:
        return f'{self.name}'
