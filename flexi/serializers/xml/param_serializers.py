import lxml.objectify

from flexi.serializers.xml.exceptions import UnsupportedParamTypeException
from flexi.serializers.xml.exceptions import UnsupportedLeafException


class BasicParamSerializer(object):

    def serialize_leaf_into_param(self, name, value, element):
        param_element = lxml.objectify.E.param(str(value), name=name, type=self.param_type)
        element.append(param_element)


class LongParamSerializer(BasicParamSerializer):

    @staticmethod
    def serialize_param_into_leaf(param_element, tree):
        tree[param_element.get('name')] = int(param_element.pyval)

    @property
    def param_type(self):
        return 'long'

    @property
    def python_type(self):
        return int


class DoubleParamSerializer(BasicParamSerializer):

    @staticmethod
    def serialize_param_into_leaf(param_element, tree):
        tree[param_element.get('name')] = float(param_element.pyval)

    @property
    def param_type(self):
        return 'double'

    @property
    def python_type(self):
        return float


class StringParamSerializer(BasicParamSerializer):

    @staticmethod
    def serialize_param_into_leaf(param_element, tree):
        tree[param_element.get('name')] = str(param_element.pyval)

    @property
    def param_type(self):
        return 'string'

    @property
    def python_type(self):
        return str


SERIALIZERS = [LongParamSerializer(),
               DoubleParamSerializer(),
               StringParamSerializer()]


def get_param_serializer(param_type):
    # Find the serializer with the given param type
    for serializer in SERIALIZERS:
        if param_type == serializer.param_type:
            return serializer
    raise UnsupportedParamTypeException(param_type)


def get_leaf_serializer(python_type):
    # Find the serializer with the given param type
    for serializer in SERIALIZERS:
        if serializer.python_type is python_type:
            return serializer
    raise UnsupportedLeafException(str(python_type))
