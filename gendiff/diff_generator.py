def build_diff(parced_data1: dict, parced_data2: dict):
    diff = []
    sorted_keys = sorted(
        set(parced_data1.keys()).union(set(parced_data2.keys())))

    operations = {
        'add': handle_addition,
        'remove': handle_removal,
        'nested': handle_nested,
        'same': handle_same,
        'changed': handle_changed
    }

    for key in sorted_keys:
        if key not in parced_data1:
            diff.append(operations['add'](key, parced_data2[key]))
        elif key not in parced_data2:
            diff.append(operations['remove'](key, parced_data1[key]))
        elif isinstance(parced_data1[key], dict) and \
                isinstance(parced_data2[key], dict):
            child = build_diff(parced_data1[key], parced_data2[key])
            diff.append(operations['nested'](key, child))
        elif parced_data1[key] == parced_data2[key]:
            diff.append(operations['same'](key, parced_data1[key]))
        else:
            diff.append(operations['changed'](
                key, parced_data1[key], parced_data2[key]))

    return diff


def handle_addition(key, value):
    return {'key': key, 'operation': 'add', 'new': value}


def handle_removal(key, value):
    return {'key': key, 'operation': 'removed', 'old': value}


def handle_nested(key, value):
    return {'key': key, 'operation': 'nested', 'value': value}


def handle_same(key, value):
    return {'key': key, 'operation': 'same', 'value': value}


def handle_changed(key, old_value, new_value):
    return {'key': key, 'operation': 'changed',
            'old': old_value, 'new': new_value}
