import os
import json
import yaml
import pytest
from gendiff.build_diff import generate_diff
from gendiff.formater.stylish import format as stylish_format
from gendiff.formater.json_formatter import format as json_format
from gendiff.formater.plain import format as plain_format

# Получаем абсолютный путь к текущему файлу
current_dir = os.path.abspath(__file__)

# Получаем абсолютный путь к папке fixtures от текущего файла
fixtures_dir = os.path.join(os.path.dirname(current_dir), 'fixtures')

# Функции для загрузки JSON, YAML, TXT файлов


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def load_text(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Создание фикстуры для хранения путей к файлам


@pytest.fixture
def data_files():
    return {
        'json1_flat': os.path.join(fixtures_dir, 'file1.json'),
        'json2_flat': os.path.join(fixtures_dir, 'file2.json'),
        'yml1_flat': os.path.join(fixtures_dir, 'file1.yml'),
        'yml2_flat': os.path.join(fixtures_dir, 'file2.yml'),
        'json1_rec': os.path.join(fixtures_dir, 'rec_struct1.json'),
        'json2_rec': os.path.join(fixtures_dir, 'rec_struct2.json'),
        'yml1_rec': os.path.join(fixtures_dir, 'rec_struct1.yml'),
        'yml2_rec': os.path.join(fixtures_dir, 'rec_struct2.yml'),
        # файл с результатом рекурсия
        'result_stylish_rec': os.path.join(fixtures_dir,
                                           'result_stylish.txt'),
        'result_plain_rec': os.path.join(fixtures_dir,
                                         'result_plain.txt'),
        'result_json_rec': os.path.join(fixtures_dir,
                                        'result_json.txt'),
        # файл с результатом плоских
        'result_stylish_flat': os.path.join(fixtures_dir,
                                            'result_stylish_flat.txt'),
        'result_plain_flat': os.path.join(fixtures_dir,
                                          'result_plain_flat.txt'),
        'result_json_flat': os.path.join(fixtures_dir,
                                         'result_json_flat.txt'),
    }

# Тесты плоских файлов формат stylish


@pytest.mark.parametrize("file1_key, file2_key, expected_key", [
    ('json1_flat', 'json2_flat', 'result_stylish_flat'),
    ('yml1_flat', 'yml2_flat', 'result_stylish_flat'),
    ('yml1_flat', 'json2_flat', 'result_stylish_flat'),
])
def test_stylish_format_flat(file1_key, file2_key, expected_key, data_files):
    file1_path = data_files[file1_key]
    file2_path = data_files[file2_key]
    expected_output_path = data_files[expected_key]

    if file1_path.endswith('.json'):
        file1 = load_json(file1_path)
        file2 = load_json(file2_path)
    elif file1_path.endswith('.yml') or file1_path.endswith('.yaml'):
        file1 = load_yaml(file1_path)
        file2 = load_yaml(file2_path)

    differences = generate_diff(file1, file2)
    formatted_diff = stylish_format(differences)

    expected_output = load_text(expected_output_path)
    assert formatted_diff == expected_output
    assert formatted_diff == expected_output

# Тесты плоских файлов формат plain


@pytest.mark.parametrize("file1_key, file2_key, expected_key", [
    ('json1_flat', 'json2_flat', 'result_plain_flat'),
    ('yml1_flat', 'yml2_flat', 'result_plain_flat'),
    ('yml1_flat', 'json2_flat', 'result_plain_flat'),
])
def test_plain_format_flat(file1_key, file2_key, expected_key, data_files):
    file1_path = data_files[file1_key]
    file2_path = data_files[file2_key]
    expected_output_path = data_files[expected_key]

    if file1_path.endswith('.json'):
        file1 = load_json(file1_path)
        file2 = load_json(file2_path)
    elif file1_path.endswith('.yml') or file1_path.endswith('.yaml'):
        file1 = load_yaml(file1_path)
        file2 = load_yaml(file2_path)

    differences = generate_diff(file1, file2)
    formatted_diff = plain_format(differences)

    expected_output = load_text(expected_output_path)
    assert formatted_diff == expected_output
    assert formatted_diff == expected_output

# Тесты плоских файлов формат json


@pytest.mark.parametrize("file1_key, file2_key, expected_key", [
    ('json1_flat', 'json2_flat', 'result_json_flat'),
    ('yml1_flat', 'yml2_flat', 'result_json_flat'),
    ('yml1_flat', 'json2_flat', 'result_json_flat'),
])
def test_json_format_flat(file1_key, file2_key, expected_key, data_files):
    file1_path = data_files[file1_key]
    file2_path = data_files[file2_key]
    expected_output_path = data_files[expected_key]

    if file1_path.endswith('.json'):
        file1 = load_json(file1_path)
        file2 = load_json(file2_path)
    elif file1_path.endswith('.yml') or file1_path.endswith('.yaml'):
        file1 = load_yaml(file1_path)
        file2 = load_yaml(file2_path)

    differences = generate_diff(file1, file2)
    formatted_diff = json_format(differences)

    expected_output = load_text(expected_output_path)
    assert formatted_diff == expected_output
    assert formatted_diff == expected_output


# Тесты рекурсия файлов формат stylish


@pytest.mark.parametrize("file1_key, file2_key, expected_key", [
    ('json1_rec', 'json2_rec', 'result_stylish_rec'),
    ('yml1_rec', 'yml2_rec', 'result_stylish_rec'),
    ('yml1_rec', 'json2_rec', 'result_stylish_rec'),
])
def test_stylish_format_rec(file1_key, file2_key, expected_key, data_files):
    file1_path = data_files[file1_key]
    file2_path = data_files[file2_key]
    expected_output_path = data_files[expected_key]

    if file1_path.endswith('.json'):
        file1 = load_json(file1_path)
        file2 = load_json(file2_path)
    elif file1_path.endswith('.yml') or file1_path.endswith('.yaml'):
        file1 = load_yaml(file1_path)
        file2 = load_yaml(file2_path)

    differences = generate_diff(file1, file2)
    formatted_diff = stylish_format(differences)

    expected_output = load_text(expected_output_path)
    assert formatted_diff == expected_output
    assert formatted_diff == expected_output


# Тесты рекурсия файлов формат plain


@pytest.mark.parametrize("file1_key, file2_key, expected_key", [
    ('json1_rec', 'json2_rec', 'result_plain_rec'),
    ('yml1_rec', 'yml2_rec', 'result_plain_rec'),
    ('yml1_rec', 'json2_rec', 'result_plain_rec'),
])
def test_plain_format_rec(file1_key, file2_key, expected_key, data_files):
    file1_path = data_files[file1_key]
    file2_path = data_files[file2_key]
    expected_output_path = data_files[expected_key]

    if file1_path.endswith('.json'):
        file1 = load_json(file1_path)
        file2 = load_json(file2_path)
    elif file1_path.endswith('.yml') or file1_path.endswith('.yaml'):
        file1 = load_yaml(file1_path)
        file2 = load_yaml(file2_path)

    differences = generate_diff(file1, file2)
    formatted_diff = plain_format(differences)

    expected_output = load_text(expected_output_path)
    assert formatted_diff == expected_output
    assert formatted_diff == expected_output


# Тесты рекурсия файлов формат json


@pytest.mark.parametrize("file1_key, file2_key, expected_key", [
    ('json1_rec', 'json2_rec', 'result_json_rec'),
    ('yml1_rec', 'yml2_rec', 'result_json_rec'),
    ('yml1_rec', 'json2_rec', 'result_json_rec'),
])
def test_json_format_rec(file1_key, file2_key, expected_key, data_files):
    file1_path = data_files[file1_key]
    file2_path = data_files[file2_key]
    expected_output_path = data_files[expected_key]

    if file1_path.endswith('.json'):
        file1 = load_json(file1_path)
        file2 = load_json(file2_path)
    elif file1_path.endswith('.yml') or file1_path.endswith('.yaml'):
        file1 = load_yaml(file1_path)
        file2 = load_yaml(file2_path)

    differences = generate_diff(file1, file2)
    formatted_diff = json_format(differences)

    expected_output = load_text(expected_output_path)
    assert formatted_diff == expected_output
    assert formatted_diff == expected_output


if __name__ == "__main__":
    pytest.main()
