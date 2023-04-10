import json


def generate_diff(file1, file2):
    content_1 = json.load(open(file1))
    content_2 = json.load(open(file2))
    result = '{\n'
    data = set(content_1.keys()) | set(content_2.keys())
    for key in sorted(data):
        if key in content_1 and key in content_2:
            if content_1[key] == content_2[key]:
                result += f'    {key}: {content_2[key]}\n'
            else:
                result += f'  - {key}: {content_1[key]}\n' \
                          f'  + {key}: {content_2[key]}\n'
        if key in content_1 and key not in content_2:
            result += f'  - {key}: {content_1[key]}\n'
        elif key in content_2 and key not in content_1:
            result += f'  + {key}: {content_2[key]}\n'
    result += '}'
    return result
