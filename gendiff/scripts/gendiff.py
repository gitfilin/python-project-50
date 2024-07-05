from gendiff.cli import parse_arguments
from gendiff.parser import parser_checks_path
from gendiff.build_diff import generate_diff
from gendiff.formater import get_formatter


def main():
    args = parse_arguments()

    # Позиционные аргументы
    file1 = args.first_file
    file2 = args.second_file

    # Опциональный аргумент для форматирования (по умолчанию "stylish")
    output_format = args.format

    # Получение данных из файлов
    data1, data2 = parser_checks_path(file1, file2)

    # Генерация разницы
    diff = generate_diff(data1, data2)

    # Получение форматтера
    formatter = get_formatter(output_format)

    # Форматирование и вывод разницы
    formatted_diff = formatter(diff)
    print(formatted_diff)


if __name__ == '__main__':
    main()
