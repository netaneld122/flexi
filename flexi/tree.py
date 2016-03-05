import pprint
import collections

from exceptions import SubTreeAlreadyExistsException


class Tree(object):

    def __init__(self):
        # This is the proper way to use a member without causing an infinite recursive call (due to __setattr__)
        self.__dict__['_ordered_dict'] = collections.OrderedDict()

    def __getattr__(self, key):
        ordered_dict = self.__dict__['_ordered_dict']
        return ordered_dict[key]

    def __setattr__(self, key, value):
        ordered_dict = self.__dict__['_ordered_dict']
        ordered_dict[key] = value

    def __delattr__(self, key):
        ordered_dict = self.__dict__['_ordered_dict']
        del ordered_dict[key]

    def __getitem__(self, key):
        return self.__getattr__(key)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __iter__(self):
        ordered_dict = self.__dict__['_ordered_dict']
        return ordered_dict.iterkeys()

    def __contains__(self, key):
        ordered_dict = self.__dict__['_ordered_dict']
        return key in ordered_dict

    def __eq__(self, other):
        ordered_dict = self.__dict__['_ordered_dict']
        return ordered_dict == other.__dict__['_ordered_dict']

    def __ne__(self, other):
        return not self.__eq__(other)

    def __dir__(self):
        ordered_dict = self.__dict__['_ordered_dict']
        return ordered_dict.keys()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        ordered_dict = self.__dict__['_ordered_dict']
        # pprint does not support ordered dicts
        return pprint.pformat(dict(ordered_dict.items()), width=1)


class RootTree(Tree):
    pass


def create_sub_tree(root, key):
    ordered_dict = root.__dict__['_ordered_dict']

    # Make sure the first sub key does match any sub tree
    sub_keys = key.split('.')
    if sub_keys[0] in ordered_dict:
        raise SubTreeAlreadyExistsException(key)

    # Create all sub trees
    current_dict = ordered_dict
    for sub_key in sub_keys:
        new_tree = Tree()
        current_dict[sub_key] = new_tree
        current_dict = new_tree.__dict__['_ordered_dict']

    return new_tree
