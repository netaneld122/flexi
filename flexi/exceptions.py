class TreeAlreadyExistsException(Exception):

    def __init__(self, key):
        super(TreeAlreadyExistsException, self).__init__(key)
