import os
import yaml
import json


def parse_content(content, ext: str) -> dict:
    # Парсит содержимое файла в зависимости от его типа
    if ext in ['yaml', 'yml']:
        return yaml.safe_load(content)
    elif ext == 'json':
        return json.loads(content)
    else:
        raise ValueError(f"Неподдерживаемый формат файла: {ext}")


def get_content(file_path: str) -> dict:
    # Загружает содержимое файла в зависимости от его типа
    try:
        _, ext = os.path.splitext(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return parse_content(content, ext[1:])
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файл не найден: {e}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка при разборе JSON: {e}")
    except yaml.YAMLError as e:
        raise ValueError(f"Ошибка при разборе YAML: {e}")


def parser_checks_path(file1_path: str, file2_path: str) -> tuple:
    # Загружает файлы по указанному пути
    try:
        data1 = get_content(file1_path)
        data2 = get_content(file2_path)
        return data1, data2
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise
