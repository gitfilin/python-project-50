import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    # Позиционные аргументы
    parser.add_argument('first_file', type=str, help='path to first file')
    parser.add_argument('second_file', type=str, help='path to second file')

    # Опциональный аргумент для форматирования (по умолчанию "stylish")
    parser.add_argument('-f', '--format', default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output (default: stylish)')

    # Версия программы
    parser.add_argument('-V', '--version', action='version',
                        version='gendiff 1.0',
                        help='output the version number')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    import sys
    sys.argv = ['gendiff/cli.py', 'tests/fixtures/file1.json',
                'tests/fixtures/file2.json', '-f', 'stylish']
    args = parse_arguments()
    print(args)
