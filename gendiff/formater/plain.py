def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, int):
        return value
    return f"'{value}'"


def format(diff, path=""):
    lines = []
    for key, value in diff.items():
        property_path = f"{path}{key}"

        if value['status'] == 'children':
            nested_lines = format(value['diff'], f"{property_path}.")
            lines.append(nested_lines)
        elif value['status'] == 'added':
            lines.append(f"Property '{property_path}' was added with value: "
                         f"{format_value(value['value'])}"
                         )
        elif value['status'] == 'removed':
            lines.append(f"Property '{property_path}' was removed")
        elif value['status'] == 'changed':
            lines.append(
                f"Property '{property_path}' was updated. From "
                f"{format_value(value['old'])} to {format_value(value['new'])}"
            )

    return '\n'.join(lines)
