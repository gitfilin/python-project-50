from typing import Any

DEFAULT_INDENT = 4


def to_str(value: Any, depth: int) -> str:
    if isinstance(value, dict):
        return format_dict(value, depth)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def format_dict(value: dict, depth: int) -> str:
    lines = ['{']
    for key, nested_value in value.items():
        if isinstance(nested_value, dict):
            new_value = to_str(nested_value, depth + DEFAULT_INDENT)
            lines.append(f"{' ' * depth}    {key}: {new_value}")
        else:
            lines.append(
                f"{' ' * depth}    {key}: {to_str(nested_value, depth)}")
    lines.append(f'{" " * depth}}}')
    return '\n'.join(lines)


def format_line(dictionary: dict, key: str, depth: int, sign: str) -> str:
    value = to_str(dictionary[key], depth + DEFAULT_INDENT)
    return f'{" " * depth}{sign}{dictionary["key"]}: {value}'


def build_stylish_same(dictionary: dict, depth: int) -> str:
    return format_line(dictionary, 'value', depth, sign='    ')


def build_stylish_add(dictionary: dict, depth: int) -> str:
    return format_line(dictionary, 'new', depth, sign='  + ')


def build_stylish_removed(dictionary: dict, depth: int) -> str:
    return format_line(dictionary, 'old', depth, sign='  - ')


def build_stylish_changed(dictionary: dict, depth: int) -> str:
    lines = [
        format_line(dictionary, 'old', depth, sign='  - '),
        format_line(dictionary, 'new', depth, sign='  + ')
    ]
    return '\n'.join(lines)


def build_stylish_nested(dictionary: dict, depth: int) -> str:
    new_value = build_stylish_iter(dictionary['value'], depth + DEFAULT_INDENT)
    return f'{" " * depth}    {dictionary["key"]}: {new_value}'


def build_stylish_iter(diff: dict, depth=0) -> str:
    lines = ['{']
    for dictionary in diff:
        operation = dictionary['operation']
        if operation == 'same':
            lines.append(build_stylish_same(dictionary, depth))
        elif operation == 'add':
            lines.append(build_stylish_add(dictionary, depth))
        elif operation == 'removed':
            lines.append(build_stylish_removed(dictionary, depth))
        elif operation == 'changed':
            lines.append(build_stylish_changed(dictionary, depth))
        elif operation == 'nested':
            lines.append(build_stylish_nested(dictionary, depth))

    lines.append(f'{" " * depth}}}')
    return '\n'.join(lines)


def format(diff: dict) -> str:
    return build_stylish_iter(diff)
