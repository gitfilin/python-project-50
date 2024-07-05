from .cli import parse_arguments
from .parser import parser_checks_path
from .build_diff import generate_diff as build_diff
from .formater import get_formatter


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1, data2 = parser_checks_path(file_path1, file_path2)
    diff = build_diff(data1, data2)
    formatter = get_formatter(format_name)
    return formatter(diff)


__all__ = ['parse_arguments', 'parser_checks_path',
           'generate_diff', 'get_formatter']
