import os
import json
import yaml
import sys

DEFAULT_PATH = 'tests/fixtures'  # Стандартный путь для поиска файлов


def parser_checks_file_type(file_path: str) -> dict:
    """Проверяем тип файла и возвращаем его содержимое в виде словаря."""
    _, ext = os.path.splitext(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        if ext.lower() in ['.yaml', '.yml']:
            return yaml.safe_load(file)
        elif ext.lower() == '.json':
            return json.load(file)
        else:
            sys.exit(f"Неподдерживаемый формат файла: {ext}")


def parser_checks_path(file1: str, file2: str) -> tuple:
    # Проверяем, являются ли входные данные абсолютными путями
    is_absolute_path1 = os.path.isabs(file1)
    is_absolute_path2 = os.path.isabs(file2)

    # Определяем фактические пути к файлам
    file_path1 = file1 if is_absolute_path1 else os.path.join(
        DEFAULT_PATH, file1)
    file_path2 = file2 if is_absolute_path2 else os.path.join(
        DEFAULT_PATH, file2)

    try:
        data1 = parser_checks_file_type(file_path1)
        data2 = parser_checks_file_type(file_path2)
        return data1, data2

    except FileNotFoundError:
        sys.exit("Невозможно открыть файл")
    except json.JSONDecodeError:
        sys.exit("Ошибка при разборе JSON")
    except yaml.YAMLError:
        sys.exit("Ошибка при разборе YAML")
