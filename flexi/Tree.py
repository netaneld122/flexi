import collections


class Tree(object):

    def __init__(self):
        # This is the proper way to use a member without causing an infinite recursive call (due to __setattr__)
        self.__dict__['data'] = collections.OrderedDict()

    def __getattr__(self, key):
        data = self.__dict__['data']

        # Hack to ignore ipython calls to __getattr__
        if key == '_ipython_display_':
            return object.__getattr__(key)

        if key not in data:
            data[key] = Tree()
        return data[key]

    def __setattr__(self, key, value):
        data = self.__dict__['data']
        data[key] = value

    def __delattr__(self, key):
        data = self.__dict__['data']
        del data[key]

    def __getitem__(self, key):
        return self.__getattr__(key)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __iter__(self):
        data = self.__dict__['data']
        return data.iterkeys()

    def __contains__(self, key):
        data = self.__dict__['data']
        return key in data
