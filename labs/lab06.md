# Задачи по Теми 13 и 14

- Рефакторирайте скрипта [lab06.py](https://github.com/fmipython/PythonCourse2023/blob/master/labs/lab06.py), така че да следва правилата за качествен код, както и PEP8 стандарта (очакваме оценка от pylint >= 9).
- Напишете unit тестове за рефакторирания скрипт (очакваме 90% code coverage).

## Оценяване:

- Рефакториране и качествен код (4.5т.)
- Тестове (1.5т)

## Структура:
Структурата на решението ви се очаква да е следната

```bash
labs
├── lab06.md
├── lab06.py
├── lab06.pylintrc
└── lab06_solution
    ├── src
    └── tst
```


## Pylint:
За изпълнение на pylint, използвайте дадения pylintrc файл (файл, съдържащ проверките на които трябва да отговаря кода): `pylint src --rcfile ../lab06.pylintrc`

## Coverage:
За проверка на code coverage, трябва да инсталирате библиотеката `coverage`. Използвайте следните команди `coverage run --source="src" -m unittest discover -s "tst"` и `coverage report -m`