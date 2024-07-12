INDENTATION = '    '   # Отступ для каждого уровня вложенности
ADDED_MARKER = '+ '    # Маркер для добавленных значений
REMOVED_MARKER = '- '  # Маркер для удаленных значений

# Словарь с маркерами для каждого статуса
STATUS_MARKERS = {
    'added': ADDED_MARKER,
    'removed': REMOVED_MARKER,
    'unchanged': '  ',
    'children': '  ',
    'changed': '  '
}


def format(diff):
    # форматируем вывод
    lines = make_lines(diff)
    output = '{\n' + '\n'.join(lines) + '\n}'
    return output


def make_lines(differences, depth=1):
    lines = []
    base_indent = INDENTATION * (depth - 1)

    for key, value in differences.items():
        status = value['status']

        if status == 'children':
            lines.append(f'{base_indent}{INDENTATION}{key}: {{')
            nested_lines = make_lines(value['diff'], depth + 1)
            lines.extend(nested_lines)
            lines.append(f'{base_indent}{INDENTATION}}}')
        elif status == 'unchanged':
            lines.append(
                f'{base_indent}{INDENTATION}{key}: '
                f'{format_value(value["value"], depth)}'
            )
        elif status == 'changed':
            lines.append(format_changed(key, value, depth))
        elif status in ['added', 'removed']:
            lines.append(format_added_removed(key, value, depth))

    return lines


def format_changed(key, value, depth):
    """
    Эта функция форматирует строки для измененных значений (status == 'changed')
    Она проверяет старое (old_value) и новое (new_value) значения.
    """
    base_indent = INDENTATION * (depth - 1)
    lines = []
    old_value = value["old"]
    new_value = value["new"]
    lines.append(
        f'{base_indent}{INDENTATION[:-2]}{REMOVED_MARKER}{key}: '
        f'{format_value(old_value, depth)}'
    )
    lines.append(
        f'{base_indent}{INDENTATION[:-2]}{ADDED_MARKER}{key}: '
        f'{format_value(new_value, depth)}'
    )
    return '\n'.join(lines)


def format_added_removed(key, value, depth):
    # Эта функция форматирует строки для added и removed значений.
    base_indent = INDENTATION * (depth - 1)
    status = value['status']
    marker = STATUS_MARKERS[status]
    return (
        f'{base_indent}{INDENTATION[:-2]}{marker}{key}: '
        f'{format_value(value["value"], depth)}'
    )


def format_value(value, depth):
    # Эта функция форматирует значение в строку в зависимости от его типа
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        # Форматируем словарь в виде строки
        lines = []
        base_indent = INDENTATION * depth
        for k, v in value.items():
            if isinstance(v, dict):
                lines.append(f'{base_indent}{INDENTATION}{k}: '
                             f'{format_value(v, depth + 1)}'
                             )
            else:
                lines.append(f'{base_indent}{INDENTATION}{k}: '
                             f'{format_value(v, depth + 1)}'
                             )
        return '{\n' + '\n'.join(lines) + '\n' + base_indent + '}'
    else:
        return str(value)
