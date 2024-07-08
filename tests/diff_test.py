import os
import pytest
from gendiff.scripts.gendiff import generate_diff


# Получаем абсолютный путь к текущему файлу
current_dir = os.path.abspath(__file__)

# Получаем абсолютный путь к папке fixtures от текущего файла
fixtures_dir = os.path.join(os.path.dirname(current_dir), 'fixtures')

# Функция для загрузки текстовых файлов


def load_text(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Создание фикстуры для хранения путей к файлам


@pytest.fixture
def data_files():
    files = {
        'json1_flat': 'file1.json',
        'json2_flat': 'file2.json',
        'yml1_flat': 'file1.yml',
        'yml2_flat': 'file2.yml',
        'json1_rec': 'rec_struct1.json',
        'json2_rec': 'rec_struct2.json',
        'yml1_rec': 'rec_struct1.yml',
        'yml2_rec': 'rec_struct2.yml',
        # файл с результатом рекурсия
        'result_stylish_rec': 'result_stylish.txt',
        'result_plain_rec': 'result_plain.txt',
        'result_json_rec': 'result_json.txt',
        # файл с результатом плоских
        'result_stylish_flat': 'result_stylish_flat.txt',
        'result_plain_flat': 'result_plain_flat.txt',
        'result_json_flat': 'result_json_flat.txt',
    }

    # пути к файлам
    for key in files:
        files[key] = os.path.join(fixtures_dir, files[key])
    return files

# Тест для generate_diff


@pytest.mark.parametrize("file1_key, file2_key, expected_key, format_name", [
    ('json1_flat', 'json2_flat', 'result_stylish_flat', 'stylish'),
    ('yml1_flat', 'yml2_flat', 'result_stylish_flat', 'stylish'),
    ('json1_flat', 'yml2_flat', 'result_stylish_flat', 'stylish'),
    ('json1_flat', 'json2_flat', 'result_plain_flat', 'plain'),
    ('yml1_flat', 'yml2_flat', 'result_plain_flat', 'plain'),
    ('json1_flat', 'yml2_flat', 'result_plain_flat', 'plain'),
    ('json1_flat', 'json2_flat', 'result_json_flat', 'json'),
    ('yml1_flat', 'yml2_flat', 'result_json_flat', 'json'),
    ('json1_flat', 'yml2_flat', 'result_json_flat', 'json'),
    # рекурсия
    ('json1_rec', 'json2_rec', 'result_stylish_rec', 'stylish'),
    ('yml1_rec', 'yml2_rec', 'result_stylish_rec', 'stylish'),
    ('json1_rec', 'yml2_rec', 'result_stylish_rec', 'stylish'),
    ('json1_rec', 'json2_rec', 'result_plain_rec', 'plain'),
    ('yml1_rec', 'yml2_rec', 'result_plain_rec', 'plain'),
    ('json1_rec', 'yml2_rec', 'result_plain_rec', 'plain'),
    ('json1_rec', 'json2_rec', 'result_json_rec', 'json'),
    ('yml1_rec', 'yml2_rec', 'result_json_rec', 'json'),
    ('json1_rec', 'yml2_rec', 'result_json_rec', 'json'),
])
def test_generate_diff(file1_key, file2_key, expected_key, format_name,
                       data_files):
    file1_path = data_files[file1_key]
    file2_path = data_files[file2_key]
    expected_output_path = data_files[expected_key]

    differences = generate_diff(file1_path, file2_path, format_name=format_name)
    expected_output = load_text(expected_output_path)
    assert differences == expected_output


if __name__ == "__main__":
    pytest.main()
