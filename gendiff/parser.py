import os
import json
import yaml

DEFAULT_PATH = 'tests/fixtures'


def parse_file(file_path: str) -> dict:
    """Проверяем тип файла и возвращаем его содержимое в виде словаря."""
    _, ext = os.path.splitext(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        if ext in ['.yaml', '.yml']:
            return yaml.safe_load(file)
        elif ext == '.json':
            return json.load(file)
        else:
            raise ValueError(f"Неподдерживаемый формат файла: {ext}")


def parser(file1: str, file2: str) -> tuple:
    # Проверяем, являются ли входные данные абсолютными путями
    is_absolute_path1 = os.path.isabs(file1)
    is_absolute_path2 = os.path.isabs(file2)

    # Определяем фактические пути к файлам
    file_path1 = file1 if is_absolute_path1 else os.path.join(
        DEFAULT_PATH, file1)
    file_path2 = file2 if is_absolute_path2 else os.path.join(
        DEFAULT_PATH, file2)

    try:
        data1 = parse_file(file_path1)
        data2 = parse_file(file_path2)
        return data1, data2

    except FileNotFoundError:
        print("Невозможно открыть файл")
    except json.JSONDecodeError:
        print("Ошибка при разборе JSON")
    except yaml.YAMLError:
        print("Ошибка при разборе YAML")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Ошибка при работе с файлом: {e}")

    return None, None
