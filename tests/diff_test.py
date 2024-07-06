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

# Функции для загрузки JSON и YAML файлов


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Создание фикстуры для хранения путей к файлам


@pytest.fixture
def data_files():
    return {
        'json1': os.path.join(fixtures_dir, 'file1.json'),
        'json2': os.path.join(fixtures_dir, 'file2.json'),
        'yml1': os.path.join(fixtures_dir, 'file1.yml'),
        'yml2': os.path.join(fixtures_dir, 'file2.yml'),
        'json1_recursive': os.path.join(fixtures_dir, 'rec_struct1.json'),
        'json2_recursive': os.path.join(fixtures_dir, 'rec_struct2.json'),
        'yml1_recursive': os.path.join(fixtures_dir, 'rec_struct1.yml'),
        'yml2_recursive': os.path.join(fixtures_dir, 'rec_struct2.yml')
    }


# Тест для stylish_format
@pytest.mark.parametrize("file1_key, file2_key, expected_output", [
    ('json1', 'json2', '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''),
    ('yml1', 'yml2', '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''),
    ('json1', 'yml2', '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''),
    ('json1_recursive', 'json2_recursive', '''{
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
}'''),
])
def test_stylish_format(file1_key, file2_key, expected_output, data_files):
    file1_path = data_files[file1_key]
    file2_path = data_files[file2_key]

    if file1_path.endswith('.json'):
        file1 = load_json(file1_path)
        file2 = load_json(file2_path)
    elif file1_path.endswith('.yml') or file1_path.endswith('.yaml'):
        file1 = load_yaml(file1_path)
        file2 = load_yaml(file2_path)

    differences = generate_diff(file1, file2)
    formatted_diff = stylish_format(differences)
    assert formatted_diff == expected_output

# Тест для json_format


@pytest.mark.parametrize("file1_key, file2_key, expected_output", [
    ('json1', 'json2', '''{
    "follow": {
        "status": "removed",
        "value": false
    },
    "host": {
        "status": "unchanged",
        "value": "hexlet.io"
    },
    "proxy": {
        "status": "removed",
        "value": "123.234.53.22"
    },
    "timeout": {
        "status": "changed",
        "old": 50,
        "new": 20
    },
    "verbose": {
        "status": "changed",
        "old": null,
        "new": true
    }
}'''),
    ('yml1', 'yml2', '''{
    "follow": {
        "status": "removed",
        "value": false
    },
    "host": {
        "status": "unchanged",
        "value": "hexlet.io"
    },
    "proxy": {
        "status": "removed",
        "value": "123.234.53.22"
    },
    "timeout": {
        "status": "changed",
        "old": 50,
        "new": 20
    },
    "verbose": {
        "status": "changed",
        "old": null,
        "new": true
    }
}'''),
    ('yml1', 'json2', '''{
    "follow": {
        "status": "removed",
        "value": false
    },
    "host": {
        "status": "unchanged",
        "value": "hexlet.io"
    },
    "proxy": {
        "status": "removed",
        "value": "123.234.53.22"
    },
    "timeout": {
        "status": "changed",
        "old": 50,
        "new": 20
    },
    "verbose": {
        "status": "changed",
        "old": null,
        "new": true
    }
}'''), ('yml1_recursive', 'json2_recursive', '''{
    "common": {
        "status": "children",
        "diff": {
            "follow": {
                "status": "added",
                "value": false
            },
            "setting1": {
                "status": "unchanged",
                "value": "Value 1"
            },
            "setting2": {
                "status": "removed",
                "value": 200
            },
            "setting3": {
                "status": "changed",
                "old": true,
                "new": null
            },
            "setting4": {
                "status": "added",
                "value": "blah blah"
            },
            "setting5": {
                "status": "added",
                "value": {
                    "key5": "value5"
                }
            },
            "setting6": {
                "status": "children",
                "diff": {
                    "doge": {
                        "status": "children",
                        "diff": {
                            "wow": {
                                "status": "changed",
                                "old": "",
                                "new": "so much"
                            }
                        }
                    },
                    "key": {
                        "status": "unchanged",
                        "value": "value"
                    },
                    "ops": {
                        "status": "added",
                        "value": "vops"
                    }
                }
            }
        }
    },
    "group1": {
        "status": "children",
        "diff": {
            "baz": {
                "status": "changed",
                "old": "bas",
                "new": "bars"
            },
            "foo": {
                "status": "unchanged",
                "value": "bar"
            },
            "nest": {
                "status": "changed",
                "old": {
                    "key": "value"
                },
                "new": "str"
            }
        }
    },
    "group2": {
        "status": "removed",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    "group3": {
        "status": "added",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
}'''),
    ('json1_recursive', 'json2_recursive', '''{
    "common": {
        "status": "children",
        "diff": {
            "follow": {
                "status": "added",
                "value": false
            },
            "setting1": {
                "status": "unchanged",
                "value": "Value 1"
            },
            "setting2": {
                "status": "removed",
                "value": 200
            },
            "setting3": {
                "status": "changed",
                "old": true,
                "new": null
            },
            "setting4": {
                "status": "added",
                "value": "blah blah"
            },
            "setting5": {
                "status": "added",
                "value": {
                    "key5": "value5"
                }
            },
            "setting6": {
                "status": "children",
                "diff": {
                    "doge": {
                        "status": "children",
                        "diff": {
                            "wow": {
                                "status": "changed",
                                "old": "",
                                "new": "so much"
                            }
                        }
                    },
                    "key": {
                        "status": "unchanged",
                        "value": "value"
                    },
                    "ops": {
                        "status": "added",
                        "value": "vops"
                    }
                }
            }
        }
    },
    "group1": {
        "status": "children",
        "diff": {
            "baz": {
                "status": "changed",
                "old": "bas",
                "new": "bars"
            },
            "foo": {
                "status": "unchanged",
                "value": "bar"
            },
            "nest": {
                "status": "changed",
                "old": {
                    "key": "value"
                },
                "new": "str"
            }
        }
    },
    "group2": {
        "status": "removed",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    "group3": {
        "status": "added",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
}'''),
])
def test_json_format(file1_key, file2_key, expected_output, data_files):
    file1_path = data_files[file1_key]
    file2_path = data_files[file2_key]

    if file1_path.endswith('.json'):
        file1 = load_json(file1_path)
        file2 = load_json(file2_path)
    elif file1_path.endswith('.yml') or file1_path.endswith('.yaml'):
        file1 = load_yaml(file1_path)
        file2 = load_yaml(file2_path)

    differences = generate_diff(file1, file2)
    formatted_diff = json_format(differences)
    assert formatted_diff == expected_output

# Тест для plain_format


@pytest.mark.parametrize("file1_key, file2_key, expected_output", [
    ('json1', 'json2', '''Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was updated. From null to true'''),
    ('yml1', 'yml2', '''Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was updated. From null to true'''),
    ('json1', 'yml2', '''Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was updated. From null to true'''),
    ('yml1_recursive', 'json2_recursive', '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''),
    ('json1_recursive', 'json2_recursive', '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''),
])
def test_plain_format(file1_key, file2_key, expected_output, data_files):
    file1_path = data_files[file1_key]
    file2_path = data_files[file2_key]

    if file1_path.endswith('.json'):
        file1 = load_json(file1_path)
        file2 = load_json(file2_path)
    elif file1_path.endswith('.yml') or file1_path.endswith('.yaml'):
        file1 = load_yaml(file1_path)
        file2 = load_yaml(file2_path)

    differences = generate_diff(file1, file2)
    formatted_diff = plain_format(differences)
    assert formatted_diff == expected_output


if __name__ == "__main__":
    pytest.main()
