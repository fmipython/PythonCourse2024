from lab07_solution_utils.task import Task

STORAGE_LOCATION = 'storage.json'


def read_tasks(storage_path: str = STORAGE_LOCATION) -> list[Task]:
    with open(storage_path) as fp:
        lines = fp.readlines()

    return [Task.from_json(line) for line in lines]


def reset_storage(storage_path: str = STORAGE_LOCATION):
    with open(storage_path, 'w', encoding='utf-8') as fp:
        fp.write('')


def write_tasks(current_tasks: list[Task], storage_path: str = STORAGE_LOCATION):
    content = [task.to_json() + '\n' for task in current_tasks]

    with open(storage_path, 'w+') as fp:
        for line in content:
            fp.write(line)
