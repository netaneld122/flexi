import json

from flexi import recursive_copy
from flexi.tree import Tree


def load(json_file_path):
    with open(json_file_path) as fp:
        tree = Tree()
        return recursive_copy.dict_to_tree(json.load(fp), tree)


def dump(tree, json_file_path):
    with open(json_file_path, 'w') as fp:
        d = {}
        recursive_copy.tree_to_dict(tree, d)
        return json.dump(d, fp, indent=4)
