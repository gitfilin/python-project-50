def generate_diff(dict1, dict2):
    differences = {}
    all_keys = sorted(set(dict1.keys()).union(set(dict2.keys())))

    for key in all_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)

        if isinstance(value1, dict) and isinstance(value2, dict):
            diff = generate_diff(value1, value2)
            if diff:
                differences[key] = {'status': 'children', 'diff': diff}
        else:
            diff_status = compare_values(value1, value2)
            if diff_status:
                differences[key] = diff_status
    return differences


def compare_values(value1, value2):
    if value1 == value2:
        return {'status': 'unchanged', 'value': value1}
    elif value1 is None:
        return {'status': 'added', 'value': value2}
    elif value2 is None:
        return {'status': 'removed', 'value': value1}
    else:
        return {'status': 'changed', 'old': value1, 'new': value2}
