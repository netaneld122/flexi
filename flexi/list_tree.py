from flexi.tree import Tree


class ListTree(Tree):

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__dict__['_ordered_dict'].keys()[item]
        else:
            return super(ListTree, self).__getitem__(item)

    def __setitem__(self, item, value):
        if isinstance(item, int):
            self.__dict__['_ordered_dict'].keys()[item] = value
        else:
            return super(ListTree, self).__setitem__(item, value)
