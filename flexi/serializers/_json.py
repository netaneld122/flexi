import json

from flexi import Tree


def load(json_file_path):
    with open(json_file_path) as fp:
        tree = Tree()
        return recursive_copy_dict_to_tree(json.load(fp), tree)


def dump(tree, json_file_path):
    with open(json_file_path, 'w') as fp:
        d = {}
        recursive_copy_tree_to_dict(tree, d)
        return json.dump(d, fp, indent=4)


def recursive_copy_dict_to_tree(d, tree):
    for key in d:
        if isinstance(d[key], dict):
            recursive_copy_dict_to_tree(d[key], tree[key])
        else:
            tree[key] = d[key]
    return tree


def recursive_copy_tree_to_dict(tree, d):
    for key in tree:
        if isinstance(tree[key], Tree):
            if key not in d:
                d[key] = {}
            recursive_copy_tree_to_dict(tree[key], d[key])
        else:
            d[key] = tree[key]
    return d
