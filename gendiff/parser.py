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
    _, ext = os.path.splitext(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return parse_content(content, ext[1:])
