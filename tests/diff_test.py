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


def test_generate_diff_recursive_inference():
    file1 = 'tests/fixtures/filepath1.yaml'
    file2 = 'tests/fixtures/filepath2.yaml'

    data1 = parser_checks_file_type(file1)
    data2 = parser_checks_file_type(file2)
    expected_output = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
    assert generate_diff(data1, data2) == expected_output
