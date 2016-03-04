from collections import OrderedDict

from flexi.tree import Tree
from flexi.tree import create_sub_tree


def ordered_dict_to_tree(d, tree):
    for key in d:
        if isinstance(d[key], dict):
            # Create a sub tree for the first time
            if key not in tree:
                create_sub_tree(tree, key)
            ordered_dict_to_tree(d[key], tree[key])
        else:
            tree[key] = d[key]
    return tree


def tree_to_ordered_dict(tree, d):
    for key in tree:
        if isinstance(tree[key], Tree):
            # Create a sub dict for the first time
            if key not in d:
                d[key] = OrderedDict()
            tree_to_ordered_dict(tree[key], d[key])
        else:
            d[key] = tree[key]
    return d
