import pytest
from gendiff.scripts.gendiff import generate_diff
from tests import get_path


@pytest.mark.parametrize(
    "file1, file2, formatter, expected",
    [
        ("file1.json", "file2.json", "stylish", "expected_result_simple.txt"),
        ("file3.json", "file4.json", "stylish", "expected_result_stylish.txt"),
        ("file3.json", "file4.json", "plain", "expected_result_plain.txt"),
        ("file3.json", "file4.json", "json", "expected_result.json"),
        ("file1.yml", "file2.yml", "stylish", "expected_result_stylish.txt"),
        ("file1.yml", "file2.yml", "plain", "expected_result_plain.txt"),
        ("file1.yml", "file4.json", "stylish", "expected_result_stylish.txt"),
        ("file1.yml", "file4.json", "plain", "expected_result_plain.txt"),
    ]
)
def test_generate_diff(file1, file2, formatter, expected):
    test_path1 = get_path(file1)
    test_path2 = get_path(file2)
    expected_path = get_path(expected)

    with open(expected_path, 'r') as file:
        expected_result = file.read().strip()

    assert generate_diff(test_path1, test_path2, formatter) == expected_result
