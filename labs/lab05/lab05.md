# Упражнение №5

## Накратко за задачата

Направете конзолно приложение, което да извежда trending филми и сериали, взимайки информацията от [The Movie Database API](https://developer.themoviedb.org/reference/intro/getting-started).

## Условие

В текущата директория се намира файлът `main.py`, който трябва да бъде направен да може да получава аргументи от командния ред, и при изпълнение да извежда на стандартния изход резултата от изпълнението. Точните изисквания за аргументите и изхода са описани по-долу.

**Добавяйте каквито пакети и модули сметете за необходимо към текущата директория - това е основният фокус на упражнението.** 

Работете във virtual envronment и създайте requirements.txt файл с използваните точни версии на външните библиоетки.

#### Аргументи

Аргументите на програмата ще са точно 3, които трябва да се подават от командния ред.

За взимане на подадените аргументи от командния ред, може да ползвате `sys.argv` от вградената библиотека `sys`. Това е лист от `str`-ове, като първият елемент е името на изпълнимия файл, а останалите са аргументите, подадени от командния ред, които в тази задача трябва да бъдат (в следния указан ред):

1. `tv`, `movies` или `all` (дали ще показваме само trending сериали, или филми, или без значение от вида)
2. `day` или `week` (дали ще показваме trending за деня или за седмицата)
3. `csv` или `json` (дали ще извеждаме резултата в CSV или JSON формат)

*В идеалния случай трябва да има валидация на аргументите, но това не е задължително за получаване на точките за функционалност, поради обема на задачата.*

#### API

1. API read access token **ще ви пратим в дискорд** (другият вариант е да минете сами през [процедурата за регистрация и създаване на ваш api key](https://www.themoviedb.org/signup)). Той трябва да бъде подаден във всеки request към API-то в header-а `Authorization` със стойност `Bearer ...` (където `...` е токенът).
2. Ползвайте GET trending ендпойнтите ([за "tv"](https://developer.themoviedb.org/reference/trending-tv) и [за "movie"](https://developer.themoviedb.org/reference/trending-movies)). Предайте "day" или "week" в заявките, спрямо това каква е стойността на втория аргумент. Не заявявайте повече от 1 page в request-ите.
3. Сайтът им освен да документира добре какво се очаква от request-ите и response-ите, също така и е доста интерактивен, позволяйки да си тествате на място заявките.

#### Изход

1. Изходът на програмата да съдържа за всеки филм/сериал единствено:
    1. `title` (str): неговото име
    2. `rating` (float): неговата средна потребителска оценка
2. Изходът да бъде **сортиран по `rating` в низходящ ред**.
3. Изходът да бъде във формат [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) или JSON, спрямо това каква е стойността на третия аргумент.
    * За конвертиране на `dict` или `list` до JSON `str`, можете да ползвате `json.dumps(...)` от вградената библиотека `json`.
4. Примерни изходи и в двата формата може да разгледате в `example_output/`.

## Асинхронност

Една точка ще дадем, ако в случая на `all` двете заявки (GET movie & GET TV) се изпълняват едновременно, вместо да се изчакват една друга. Препоръчваме за целта да разучите [aiohttp](https://docs.aiohttp.org/en/stable/).


## Примери

Команда:
```bash
python main.py tv day csv
```

Изход:
```csv
title,rating
South Sea Tomb,8.8
One Piece,8.728
World War II: From the Frontlines,8.7
Attack on Titan,8.668
Jujutsu Kaisen,8.568
My Demon,8.567
The Walking Dead: Daryl Dixon,8.451
Game of Thrones,8.442
High Tides,8.4
Sweet Home,8.396
Fargo,8.305
Monarch: Legacy of Monsters,8.198
Loki,8.184
Blood Coast,7.905
Doctor Who,7.9
Slow Horses,7.79
Doctor Who,7.465
My Life with the Walter Boys,6.9
Obliterated,6.55
Squid Game: The Challenge,6.25
```

Команда:
```bash
python main.py movie week json
```

Изход:
```json
[{"title": "Oppenheimer", "rating": 8.14}, {"title": "Five Nights at Freddy's", "rating": 7.844}, {"title": "Killers of the Flower Moon", "rating": 7.716}, {"title": "Mission: Impossible - Dead Reckoning Part One", "rating": 7.592}, {"title": "Leo", "rating": 7.533}, {"title": "The Hunger Games: The Ballad of Songbirds & Snakes", "rating": 7.295}, {"title": "Trolls Band Together", "rating": 7.2}, {"title": "Barbie", "rating": 7.179}, {"title": "The Creator", "rating": 7.131}, {"title": "Wonka", "rating": 7.0}, {"title": "Leave the World Behind", "rating": 6.935}, {"title": "Indiana Jones and the Dial of Destiny", "rating": 6.678}, {"title": "The Killer", "rating": 6.655}, {"title": "Wish", "rating": 6.625}, {"title": "May December", "rating": 6.613}, {"title": "The Marvels", "rating": 6.555}, {"title": "Freelance", "rating": 6.434}, {"title": "Napoleon", "rating": 6.433}, {"title": "Family Switch", "rating": 6.381}, {"title": "Candy Cane Lane", "rating": 6.339}]
```

## Оценяване

* 2 т. - за смислено разделяне на кода в допълнителни модули и пакети
* 1 т. - за коректна и пълна функционалност
* 1 т. - за коректен requirements.txt и използване на virtual environment
* 1 т. - за едновременно изпълнение на заявките при `all`
