def building_diff(dict1, dict2):
    differences = {}

    # Получаем добавленные и удаленные ключи
    added_keys, removed_keys = get_keys_difference(dict1, dict2)

    all_keys = sorted(set(dict1.keys()).union(set(dict2.keys())))

    for key in all_keys:
        value1 = dict1.get(key, "__UNDEFINED__")
        value2 = dict2.get(key, "__UNDEFINED__")

        if key in added_keys:
            differences[key] = {'status': 'added', 'value': value2}
        elif key in removed_keys:
            differences[key] = {'status': 'removed', 'value': value1}
        elif isinstance(value1, dict) and isinstance(value2, dict):
            differences[key] = {'status': 'children',
                                'diff': building_diff(value1, value2)}
        else:
            if value1 == value2:
                differences[key] = {'status': 'unchanged', 'value': value1}
            elif value1 == "__UNDEFINED__":
                differences[key] = {'status': 'added', 'value': value2}
            elif value2 == "__UNDEFINED__":
                differences[key] = {'status': 'removed', 'value': value1}
            else:
                differences[key] = {'status': 'changed',
                                    'old': value1, 'new': value2}

    return differences


def get_keys_difference(dict1, dict2):
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    added_keys = keys2 - keys1
    removed_keys = keys1 - keys2
    return sorted(added_keys), sorted(removed_keys)
