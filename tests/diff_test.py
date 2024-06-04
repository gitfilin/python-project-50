import pytest
from gendiff.diff_generator import generate_diff
from gendiff.parser import parser_checks_file_type


def test_generate_diff_flat():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'

    data1 = parser_checks_file_type(file1)
    data2 = parser_checks_file_type(file2)
    expected_output = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
    assert generate_diff(data1, data2) == expected_output


def test_flat_yaml_files():
    file1 = 'tests/fixtures/file1.yaml'
    file2 = 'tests/fixtures/file2.yaml'

    data1 = parser_checks_file_type(file1)
    data2 = parser_checks_file_type(file2)

    expected_output = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
    assert generate_diff(data1, data2) == expected_output
