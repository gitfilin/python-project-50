import os
import json
import yaml
import sys


def checks_extension_type(file_path: str) -> str:
    """Получает расширение файла."""
    _, ext = os.path.splitext(file_path)
    return ext.lower()


def load_file(file_path: str) -> dict:
    """Загружает содержимое файла в зависимости от его типа"""
    ext = checks_extension_type(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        if ext in ['.yaml', '.yml']:
            return yaml.safe_load(file)
        elif ext == '.json':
            return json.load(file)
        else:
            raise ValueError(f"Неподдерживаемый формат файла: {ext}")


def parser_checks_path(file1: str, file2: str) -> tuple:
    try:
        data1 = load_file(file1)
        data2 = load_file(file2)
        return data1, data2

    except FileNotFoundError:
        sys.exit("Невозможно открыть файл")
    except json.JSONDecodeError:
        sys.exit("Ошибка при разборе JSON")
    except yaml.YAMLError:
        sys.exit("Ошибка при разборе YAML")
