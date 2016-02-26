import pprint
import collections

from exceptions import TreeAlreadyExistsException


class Tree(object):

    def __init__(self):
        # This is the proper way to use a member without causing an infinite recursive call (due to __setattr__)
        self.__dict__['ordered_dict'] = collections.OrderedDict()

    def new(self, key):
        ordered_dict = self.__dict__['ordered_dict']
        if key in ordered_dict:
            raise TreeAlreadyExistsException(key)
        ordered_dict[key] = Tree()
        return ordered_dict[key]

    def __getattr__(self, key):
        ordered_dict = self.__dict__['ordered_dict']
        return ordered_dict[key]

    def __setattr__(self, key, value):
        ordered_dict = self.__dict__['ordered_dict']
        ordered_dict[key] = value

    def __delattr__(self, key):
        ordered_dict = self.__dict__['ordered_dict']
        del ordered_dict[key]

    def __getitem__(self, key):
        return self.__getattr__(key)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __iter__(self):
        ordered_dict = self.__dict__['ordered_dict']
        return ordered_dict.iterkeys()

    def __contains__(self, key):
        ordered_dict = self.__dict__['ordered_dict']
        return key in ordered_dict

    def __eq__(self, other):
        ordered_dict = self.__dict__['ordered_dict']
        return ordered_dict == other.__dict__['ordered_dict']

    def __ne__(self, other):
        return not self.__eq__(other)

    def __dir__(self):
        ordered_dict = self.__dict__['ordered_dict']
        return ordered_dict.keys()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        ordered_dict = self.__dict__['ordered_dict']
        # pprint does not support ordered dicts
        return pprint.pformat(dict(ordered_dict.items()), width=1)
