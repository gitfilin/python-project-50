import os
import pytest
from gendiff.diff_generator import generate_diff


def get_content(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()


def get_fixture_path(file_name):
    # Получаем абсолютный путь к текущему файлу
    current_dir = os.path.abspath(__file__)
    # Получаем абсолютный путь к папке fixtures от текущего файла
    fixtures_dir = os.path.join(os.path.dirname(current_dir), 'fixtures')
    return os.path.join(fixtures_dir, file_name)

# Тест для generate_diff


@pytest.mark.parametrize("file1, file2, expected, format_name", [
    ("file1.json", "file2.json", "result_stylish_flat.txt", "stylish"),
    ("file1.yml", "file2.yml", "result_stylish_flat.txt", "stylish"),
    ("file1.json", "file2.yml", "result_stylish_flat.txt", "stylish"),
    ("file1.json", "file2.json", "result_plain_flat.txt", "plain"),
    ("file1.yml", "file2.yml", "result_plain_flat.txt", "plain"),
    ("file1.json", "file2.yml", "result_plain_flat.txt", "plain"),
    ("file1.json", "file2.json", "result_json_flat.txt", "json"),
    ("file1.yml", "file2.yml", "result_json_flat.txt", "json"),
    ("file1.json", "file2.yml", "result_json_flat.txt", "json"),
    # рекурсия
    ("rec_struct1.json", "rec_struct2.json", "result_stylish.txt", "stylish"),
    ("rec_struct1.yml", "rec_struct2.yml", "result_stylish.txt", "stylish"),
    ("rec_struct1.json", "rec_struct2.yml", "result_stylish.txt", "stylish"),
    ("rec_struct1.json", "rec_struct2.json", "result_plain.txt", "plain"),
    ("rec_struct1.yml", "rec_struct2.yml", "result_plain.txt", "plain"),
    ("rec_struct1.json", "rec_struct2.yml", "result_plain.txt", "plain"),
    ("rec_struct1.json", "rec_struct2.json", "result_json.txt", "json"),
    ("rec_struct1.yml", "rec_struct2.yml", "result_json.txt", "json"),
    ("rec_struct1.json", "rec_struct2.yml", "result_json.txt", "json"),
])
def test_generate_diff(file1, file2, expected, format_name):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_output_path = get_fixture_path(expected)

    differences = generate_diff(file1_path, file2_path, format_name=format_name)
    expected_output = get_content(expected_output_path)
    assert differences == expected_output
