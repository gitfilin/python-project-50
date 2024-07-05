from gendiff.cli import parse_arguments
from gendiff.parser import parser_checks_path
from gendiff.generate_diff import build_diff
from gendiff.formater import get_formatter


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1, data2 = parser_checks_path(file_path1, file_path2)
    diff = build_diff(data1, data2)
    formatter = get_formatter(format_name)
    return formatter(diff)


def main():
    args = parse_arguments()

    # Позиционные аргументы
    file1 = args.first_file
    file2 = args.second_file

    # Опциональный аргумент для форматирования (по умолчанию "stylish")
    output_format = args.format

    # Генерация и вывод разницы
    diff = generate_diff(file1, file2, output_format)
    print(diff)


if __name__ == '__main__':
    main()
