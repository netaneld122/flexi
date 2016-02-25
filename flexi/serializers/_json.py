import json


def load(json_file_path):
    with open(json_file_path) as fp:
        return json.load(fp)


def dump(root, json_file_path):
    with open(json_file_path, 'w') as fp:
            return json.dump(root, fp)
