#!/usr/bin/env python3
from gendiff.cli import parse_arguments
from gendiff.parser import parser_checks_path
from gendiff.diff_generator import generate_diff
from gendiff.formater import stylish


def main():
    args = parse_arguments()
    # Позиционные аргументы
    file1 = args.first_file
    file2 = args.second_file
    # Опциональные аргументы с разными типами
    format = args.format

    # передаем данные на проверку в парсер
    data1, data2 = parser_checks_path(file1, file2)
    diff = generate_diff(data1, data2)
    print(diff)

    if args.format:
        print("Форматирование включено")


if __name__ == '__main__':
    main()
