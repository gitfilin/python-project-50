import yaml
import json
import sys


def parse_content(file, ext: str) -> dict:
    # Парсит содержимое файла в зависимости от его типа
    if ext in ['.yaml', '.yml']:
        return yaml.safe_load(file)
    elif ext == '.json':
        return json.load(file)
    else:
        raise ValueError(f"Неподдерживаемый формат файла: {ext}")


def get_content(file_path: str) -> dict:
    # Загружает содержимое файла в зависимости от его типа
    ext = file_path[file_path.rfind('.'):]
    with open(file_path, 'r', encoding='utf-8') as file:
        return parse_content(file, ext)


def parser_checks_path(file1_path: str, file2_path: str) -> tuple:
    # Загружает файлы по указанному пути в _path
    try:
        data1 = get_content(file1_path)
        data2 = get_content(file2_path)
        return data1, data2

    except FileNotFoundError:
        sys.exit("Невозможно открыть файл")
    except json.JSONDecodeError:
        sys.exit("Ошибка при разборе JSON")
    except yaml.YAMLError:
        sys.exit("Ошибка при разборе YAML")
