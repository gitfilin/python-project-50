from gendiff.cli import parse_arguments
from gendiff import generate_diff


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
