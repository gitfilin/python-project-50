def generate_diff(dict1, dict2):
    differences = {}
    all_keys = sorted(set(dict1.keys()).union(set(dict2.keys())))

    for key in all_keys:
        value1 = dict1.get(key, "__UNDEFINED__")
        value2 = dict2.get(key, "__UNDEFINED__")

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
    if value1 == "__UNDEFINED__":
        return {'status': 'added', 'value': value2}
    if value2 == "__UNDEFINED__":
        return {'status': 'removed', 'value': value1}
    if value1 == value2:
        return {'status': 'unchanged', 'value': value1}
    return {'status': 'changed', 'old': value1, 'new': value2}
