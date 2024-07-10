from . import get_content, building_diff, get_formatter


def generate_diff(file_path1, file_path2, format_name='stylish'):
    try:
        data1 = get_content(file_path1)
        data2 = get_content(file_path2)
        diff = building_diff(data1, data2)
        formatter = get_formatter(format_name)
        return formatter(diff)
    except Exception as e:
        print(f"Произошла ошибка при генерации diff: {e}")
        raise
