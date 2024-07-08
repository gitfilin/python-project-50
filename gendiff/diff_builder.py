def building_diff(dict1, dict2):
    differences = {}

    # возвращаем добавленные и удаленные ключи
    added_keys, removed_keys = get_keys_difference(dict1, dict2)

    all_keys = sorted(set(dict1.keys()).union(set(dict2.keys())))

    for key in all_keys:
        value1 = dict1.get(key, "__UNDEFINED__")
        value2 = dict2.get(key, "__UNDEFINED__")

        if key in added_keys:
            adding_keys_diff(differences, key, 'added', value2)
        elif key in removed_keys:
            adding_keys_diff(differences, key, 'removed', value1)
        elif isinstance(value1, dict) and isinstance(value2, dict):
            differences[key] = adding_children(dict1, dict2, key)
        else:
            diff_status = compare_values(value1, value2)
            if diff_status:
                differences[key] = diff_status

    return differences


def get_keys_difference(dict1, dict2):
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    added_keys = keys2 - keys1
    removed_keys = keys1 - keys2
    return sorted(added_keys), sorted(removed_keys)


def adding_keys_diff(differences, key, status, value):
    differences[key] = {'status': status, 'value': value}


def adding_children(dict1, dict2, key):
    return {'status': 'children', 'diff': building_diff(dict1[key], dict2[key])}


def compare_values(value1, value2):
    if value1 == value2:
        return {'status': 'unchanged', 'value': value1}
    if value1 == "__UNDEFINED__":
        return {'status': 'added', 'value': value2}
    if value2 == "__UNDEFINED__":
        return {'status': 'removed', 'value': value1}
    return {'status': 'changed', 'old': value1, 'new': value2}
