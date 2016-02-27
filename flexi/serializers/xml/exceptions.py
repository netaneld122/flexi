class UnsupportedElementException(Exception):

    def __init__(self, element_tag):
        super(UnsupportedElementException, self).__init__(element_tag)


class UnsupportedParamTypeException(Exception):

    def __init__(self, param_type):
        super(UnsupportedParamTypeException, self).__init__(param_type)


class UnsupportedLeafException(Exception):

    def __init__(self, key):
        super(UnsupportedLeafException, self).__init__(key)
