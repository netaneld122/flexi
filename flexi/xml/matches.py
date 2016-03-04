import lxml.objectify
import lxml.etree

from flexi.xml import serializer_registry


def xml_element_injector(element):
    def wrapper(cls):
        serializer_registry.xml_serializers.append(cls)
        cls.xml_element = element
    return wrapper


# Class decorators


def xml_element_string(element_string):
    element = lxml.etree.fromstring(element_string)
    return xml_element_injector(element)


def xml_element(tag, **attributes):
    maker = lxml.objectify.ElementMaker(annotate=False)
    element = getattr(maker, tag)(**attributes)
    return xml_element_injector(element)


def python_type(_python_type):

    def python_type_injector(cls):
        cls.python_type = _python_type
        serializer_registry.tree_serializers.append(cls)
        return cls
    return python_type_injector
