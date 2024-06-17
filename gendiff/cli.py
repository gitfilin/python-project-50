import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    # Позиционные аргументы
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    # Опциональные аргументы с разными типами форматирования, по дефолту стоит stylish
    parser.add_argument('-f', '--format', nargs='?', const='default', type=str,
                        help='set format of output')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    print(parse_arguments())
