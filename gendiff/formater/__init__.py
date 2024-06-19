from gendiff.formater.stylish import format as stylish
from gendiff.formater.plain import format as plain
from gendiff.formater.json_formatter import format as json


def get_formatter(format_name):
    if format_name == 'plain':
        return plain
    elif format_name == 'json':
        return json
    return stylish
