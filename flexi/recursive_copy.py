from flexi.tree import Tree


def dict_to_tree(d, tree):
    for key in d:
        if isinstance(d[key], dict):
            dict_to_tree(d[key], tree[key])
        else:
            tree[key] = d[key]
    return tree


def tree_to_dict(tree, d):
    for key in tree:
        if isinstance(tree[key], Tree):
            if key not in d:
                d[key] = {}
            tree_to_dict(tree[key], d[key])
        else:
            d[key] = tree[key]
    return d
