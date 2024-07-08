from gendiff.diff_generator import generate_diff
from gendiff.cli import parse_arguments


def main():
    args = parse_arguments()
    print("Arguments parsed:", args)

    file1 = args.first_file
    file2 = args.second_file
    output_format = args.format
    print("Files:", file1, file2)

    diff = generate_diff(file1, file2, output_format)
    print(diff)


if __name__ == '__main__':
    main()
