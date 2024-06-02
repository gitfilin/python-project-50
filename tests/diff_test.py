import pytest
from gendiff.diff_generator import generate_diff


def test_generate_diff():
    data1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    data2 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    expected_output = """{
    follow: False
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
    assert generate_diff(data1, data2) == expected_output
