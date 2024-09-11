# Бесеница

Проектът реализира игра на "Бесеница" с команден интерфейс. Позволява различни възможности за конфигурация, които включват нива на трудност и начин на игра (от истински играч или AI).

## Инсталация

1. Създаване на виртуална среда:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

2. Инсталация на небходимите пакети:
    1. За употреба:

    ```bash
    pip install -r requirements.txt
    ```

    2. За разработка:

    ```bash
    pip install -r requirements-dev.txt 
    ```

## Употреба

```bash
python3 main.py [name_of_config]
```

където `name_of_config` е името на конфигурационния YAML файл от директорията `configs` (без разширението).
