#!/usr/bin/env python3
from gendiff.cli import parse_arguments
from gendiff.parser import parser
from gendiff.diff_generator import generate_diff

def main():
    args = parse_arguments()
    file1 = args.first_file
    file2 = args.second_file    
    data1, data2 = parser(file1, file2)
 
    diff = generate_diff(data1, data2)
    print(diff)
    
    if args.format:
        print("Форматирование включено")


if __name__ == '__main__':
    main()
