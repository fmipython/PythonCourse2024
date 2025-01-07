# Упражнение №6

В това упражнение ще оправим бъгче, добавим нова функционалност, рефакторираме код и напишем тестове. Почти като на работа 🙃

## Съществуващ код

В папка `spaghetti-notes` се намира Python конзолно приложение - бележник. Използва се по един от следните 4 начина:

1. Добавяне на бележка

    ```bash
    python main.py add --title "Заглавие на бележката" --content "Съдържание на бележката" 
    ```

    Възможно е и да се добави срок към бележката (задачата) чрез `--due-date`.

2. Преглед на бележка

    ```bash
    python main.py view --title "Заглавие на бележката"
    ```

3. Изтриване на бележка

    ```bash
    python main.py delete --title "Заглавие на бележката"
    ```

4. Преглед на всички бележки

    ```bash
    python main.py list
    ```

## Задача

Имате няколко цели, които да изпълните, като **няма значение в какъв ред ще ги изпълните**. Препоръчваме все пак първо да оправите бъга (Цел А), за да се запознаете с кода (и проблемите му)

### Цел А: Оправяне на бъг

Получен е следният бъг от тестери (QA) на софтуера:

* Bug description:

    After creating a note without a due date, no notes are listed when displaying all notes via `list`. Additionally, when viewing the note with the `view` subcommand, no due date info is displayed.

* Steps to reproduce:

    1. `python main.py add --title "Бележка без срок" --content "Съдържание на бележката"`
    2. `python main.py list`
        * Expected output:
            ```
            Listing notes...
            - Бележка без срок (Due: None)
            ```
        * Actual output:
            ```
            Listing notes...
            ```
    3. `python main.py view --title "Бележка без срок"`
        * Expected output:
            ```
            Бележка без срок
            ---
            Съдържание на бележката
            ---
            No due date.
            ```
        * Actual output:
            ```
            Бележка без срок
            ---
            Съдържание на бележката
            ---
            ```
    
### Цел Б: Добавяне на нова функционалност

Бизнес анализаторите ни са добавили нов таск:

* Description:

    As a user, I want to be able to edit the content and/or due date of an existing note. This needs to be done through a new command `edit`.

* Acceptance criteria:

    1. The user should be able to edit the *content* and/or the *due date* of an existing note.
    2. The user should **not** be able to edit the *title* of an existing note.
    4. Upon successful edit, the user should see a message **"Note successfully edited."**
    5. If no note exists with the provided title, the user should see a message **"Note with title {title} does not exist."**
    6. If the user tries to edit a note without providing any new content or due date, the user should see a message **"No content or due date provided - no changes made to the note."**
    7. If the user wished to erase the due date of a note, they should be able to do so by providing `none` as the value of the `--due-date` argument.

* Example usage:

    ```bash
    python main.py edit --title "Some note title" --content "New content"
    #
    python main.py edit --title "Some note title" --due-date "2026-01-01"
    #
    python main.py edit --title "Some note title" --due-date none
    #
    python main.py edit --title "Some note title" --content "New content" --due-date "2026-01-01"
    #
    python main.py edit --title "Some note title" --content "New content" --due-date none
    ```

### Цел В: Рефакториране на кода

Това изискване няма как да дойде от бизнес анализаторите или QA-те във фирмата, но т.нар [tech debt](https://en.wikipedia.org/wiki/Technical_debt) (както, надяваме се, сами виждате) се е натрупал вече до пределно ниво, и трябва да се направи нещо по въпроса. Ще влезем в ролята на ваши новоназначени tech lead-ове и ще ви позволим (даже задължим) да оправите бъркотията и спагетите в съществуващия код (yes, pun intended).

Полученото можем да оценим по сравнително обективен начин, чрез `pylint`. Изпълнете следната команда (след `pip install pylint`, ако нямате инсталиран [pylint](https://pypi.org/project/pylint/)):

```bash
pylint spaghetti-notes  # ако сте над директорията на проекта
# или
pylint main.py actions/  # ако сте във директорията на проекта
```

Това ще ви изведе серия от грешки, предупрежнения, съвети и т.н. по стила на кода. Накрая ще има един ред с обща оценка от рода на `Your code has been rated at 5.89/10.`

Разбира се, трябва да го сведете до **10/10**.

### Цел Г: Писане на тестове

За да не се допускат в бъдеще глупави бъгове като този от Цел А е хубаво да се напишат тестове. В тази задача това е и почти невъзможно без изпълнението и на Цел В - двете е най-естествено да вървят ръка за ръка.

Напишете изчерпателни юнит тестове за всеки един от основните компоненти/функционалности на програмата, плюс каквито нови отделите/създадете. Използвайте който testing framework предпочитате без ограничения. 

Можете, разбира се, да създавате папки и местите файлове както прецените за удачно.

За упражнението ще изискаме и да проверявате тестовете колко реда от кода ви покриват чрез [`coverage`](https://coverage.readthedocs.io/en/7.6.10/) (инсталирате с `pip install coverage`). В [документацията](https://coverage.readthedocs.io/en/7.6.10/) е хубаво описано как се използва - общо взето в командата, с която си пускате тестовете, трябва да замените `python -m ...` с `coverage run -m ...`, а след това да пуснете `coverage report` за да видите статистика за code coverage (`coverage report -m` ви дава и кои редове са изтървани):

* Ако използвате `unittest`:

    ```bash
    coverage run -m unittest ...
    coverage report -m
    ```

* Ако използвате `pytest`:

    ```bash
    coverage run -m pytest ...
    coverage report -m
    ```

*Ако не сте сигурни какво да напишете на мястото на `...` си припомнете [лекцията за тестове](../../14%20-%20Testing/15%20-%20Testing.ipynb).*

Втората команда извежда таблица с покритието, като **изискваме на TOTAL да имате поне 80%.**

Ако сорс кодът ви се намира в директория на същото ниво на директорията с тестовете (препоръчително), можете да укажете `--source=<src директорията>.` като аргумент на `coverage run`. Справка: [тук](https://coverage.readthedocs.io/en/7.6.10/cmd.html#cmd-run).

## Оценяване

Общо макс. 3т.:

* Цел А: 0.5т. (след code review)
* Цел Б: 0.5т. (след code review)
* Цел В: 1т.   (след code review + pylint 10/10)
* Цел Г: 1т.   (след code review + coverage >= 80%)
