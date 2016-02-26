class SubTreeAlreadyExistsException(Exception):

    def __init__(self, key):
        super(SubTreeAlreadyExistsException, self).__init__(key)
