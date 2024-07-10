INDENTATION = '    '   # Отступ для каждого уровня вложенности
ADDED_MARKER = '+ '    # Маркер для добавленных значений
REMOVED_MARKER = '- '  # Маркер для удаленных значений


def format(diff):
    # форматируем вывод
    lines = make_lines(diff)
    output = '{\n' + '\n'.join(lines) + '\n}'
    return output


def make_lines(differences, depth=1):
    # Эта функция создает отформатированные строки для каждой пары ключ-значение
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
        else:
            marker = ADDED_MARKER if status == 'added' else REMOVED_MARKER
            lines.append(
                f'{base_indent}{INDENTATION[:-2]}{marker}{key}: '
                f'{format_value(value["value"], depth)}'
            )

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

    if old_value is None and new_value is True:
        lines.append(
            f'{base_indent}{INDENTATION[:-2]}{ADDED_MARKER}{key}: '
            f'{format_value(new_value, depth)}'
        )
    else:
        lines.append(
            f'{base_indent}{INDENTATION[:-2]}{REMOVED_MARKER}{key}: '
            f'{format_value(old_value, depth)}'
        )
        lines.append(
            f'{base_indent}{INDENTATION[:-2]}{ADDED_MARKER}{key}: '
            f'{format_value(new_value, depth)}'
        )

    return '\n'.join(lines)


def format_value(value, depth):
    # Эта функция форматирует значение в строку в зависимости от его типа
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return format_dict(value, depth + 1)
    else:
        return str(value)


def format_dict(value, depth):
    # Эта функция форматирует словарь value в виде строки.
    lines = []
    base_indent = INDENTATION * (depth - 1)
    for k, v in value.items():
        if isinstance(v, dict):
            lines.append(f'{base_indent}{INDENTATION}{k}: '
                         f'{format_dict(v, depth + 1)}'
                         )
        else:
            lines.append(f'{base_indent}{INDENTATION}{k}: '
                         f'{format_value(v, depth + 1)}'
                         )
    return '{\n' + '\n'.join(lines) + '\n' + INDENTATION * (depth - 1) + '}'
