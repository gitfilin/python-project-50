def generate_diff(data1: dict, data2: dict) -> str:
    # flatten_dict(data1)
    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))
    result = []

    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                result.append(f"    {key}: {data1[key]}")
            else:
                result.append(f"  - {key}: {data1[key]}")
                result.append(f"  + {key}: {data2[key]}")
        elif key in data1:
            result.append(f"  - {key}: {data1[key]}")
        else:
            result.append(f"  + {key}: {data2[key]}")

    return "{\n" + "\n".join(result) + "\n}"


def flatten_dict(nested_dict):
    flat_dict = {}
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            flat_dict.update(flatten_dict(value))
        else:
            flat_dict[key] = value
    print('подсчет', len(flat_dict))
