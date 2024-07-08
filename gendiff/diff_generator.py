from . import parser_checks_path, building_diff, get_formatter


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1, data2 = parser_checks_path(file_path1, file_path2)
    diff = building_diff(data1, data2)
    formatter = get_formatter(format_name)

    return formatter(diff)
