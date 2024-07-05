DEF = '    '  # Default indentation (4 spaces replaced by dots)
ADD = '+ '
DEL = '- '


def format(diff):
    lines = make_lines(diff)
    output = '{\n' + '\n'.join(lines) + '\n}'
    return output


def make_lines(differences, depth=1):
    lines = []
    for key, value in differences.items():
        status = value['status']
        base_indent = DEF * (depth - 1)  # Базовый отступ для всех ключей
        if status == 'children':
            lines.append(f'{base_indent}{DEF}{key}: {{')
            nested_lines = make_lines(value['diff'], depth + 1)
            lines.extend(nested_lines)
            lines.append(f'{base_indent}{DEF}}}')
        else:
            lines.append(format_line(key, value, depth))
    return lines


def format_line(key, value, depth):
    base_indent = DEF * depth  # Базовый отступ для всех ключей
    status = value['status']
    if status == 'unchanged':
        return f'{base_indent}{format_key_value(key, value["value"])}'
    elif status == 'added':
        return (
            f'{base_indent[:-4]}  {ADD}{key}: '
            f'{format_value(value["value"], depth)}'
        )
    elif status == 'removed':
        return (
            f'{base_indent[:-4]}  {DEL}{key}: '
            f'{format_value(value["value"], depth)}'
        )
    elif status == 'changed':
        return format_changed(key, value, depth)


def format_changed(key, value, depth):
    base_indent = DEF * depth
    lines = []
    lines.append(
        f'{base_indent[:-4]}  {DEL}{key}: '
        f'{format_value(value["old"], depth)}'
    )
    lines.append(
        f'{base_indent[:-4]}  {ADD}{key}: '
        f'{format_value(value["new"], depth)}'
    )
    return '\n'.join(lines)


def format_key_value(key, value):
    if isinstance(value, bool):
        return f'{key}: {str(value).lower()}'
    elif value is None:
        return f'{key}: null'
    elif isinstance(value, dict):
        # Начинаем с глубины 1 для вложенных словарей
        return format_dict(value, 1)
    else:
        return f'{key}: {value}'


def format_dict(value, depth):
    lines = []
    base_indent = DEF * depth
    for k, v in value.items():
        if isinstance(v, dict):
            lines.append(f'{base_indent}{DEF}{k}: '
                         f'{format_dict(v, depth + 1)}'
                         )
        else:
            lines.append(f'{base_indent}{DEF}{k}: '
                         f'{
                         format_value(v, depth + 1)}'
                         )
    return '{\n' + '\n'.join(lines) + '\n' + DEF * (depth - 1) + '}'


def format_value(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return format_dict(value, depth + 1)
    else:
        return str(value)
