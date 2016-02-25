import collections


class Tree(object):

    def __init__(self):
        # This is the way to use a member without causing an infinite recursive call (due to __setattr__)
        self.__dict__['data'] = collections.OrderedDict()

    def __getattr__(self, key):
        data = self.__dict__['data']
        if key not in data:
            data[key] = Tree()
        return data[key]

    def __setattr__(self, key, value):
        data = self.__dict__['data']
        data[key] = value

    def __getitem__(self, item):
        data = self.__dict__['data']
        return data[item]

    def __setitem__(self, key, value):
        data = self.__dict__['data']
        data[key] = value
