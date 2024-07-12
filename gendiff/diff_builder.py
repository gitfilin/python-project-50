def building_diff(dict1, dict2):
    differences = {}

    added_keys = set(dict2.keys()) - set(dict1.keys())
    removed_keys = set(dict1.keys()) - set(dict2.keys())
    all_keys = sorted(set(dict1.keys()).union(set(dict2.keys())))

    for key in all_keys:
        value1 = dict1.get(key, "__UNDEFINED__")
        value2 = dict2.get(key, "__UNDEFINED__")

        if key in added_keys:
            differences[key] = {'status': 'added', 'value': value2}
            continue

        if key in removed_keys:
            differences[key] = {'status': 'removed', 'value': value1}
            continue

        if value1 == value2:
            differences[key] = {'status': 'unchanged', 'value': value1}
        else:
            differences[key] = {'status': 'changed',
                                'old': value1, 'new': value2}

        if isinstance(value1, dict) and isinstance(value2, dict):
            differences[key] = {'status': 'children',
                                'diff': building_diff(value1, value2)}

    return differences
