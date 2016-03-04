import json

from collections import OrderedDict

from flexi.json import recursive_copy
from flexi.tree import Tree


def load(json_file_path):
    with open(json_file_path) as fp:
        tree = Tree()
        return recursive_copy.ordered_dict_to_tree(json.load(fp, object_pairs_hook=OrderedDict), tree)


def dump(tree, json_file_path):
    with open(json_file_path, 'w') as fp:
        d = OrderedDict()
        recursive_copy.tree_to_ordered_dict(tree, d)
        return json.dump(d, fp, indent=4)
