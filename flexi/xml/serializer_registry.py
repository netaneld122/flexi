import lxml.etree

from flexi.xml.exceptions import UnsupportedElementException
from flexi.xml.exceptions import UnsupportedPythonTypeException


# Utility functions for xml elements filtering


def lower_dict(d):
    return dict((key.lower(), d[key].lower()) for key in d)


def attributes_subset_of(attributes_a, attributes_b):
    return lower_dict(attributes_a).viewitems() <= lower_dict(attributes_b).viewitems()


def tags_match(tag_a, tag_b):
    return tag_a.lower().strip() == tag_b.lower().strip()


# Registry of serializers


# flexi.xml.matches decorators fill this list
xml_serializers = []


def get_xml_serializer(element):
    for xml_serializer in xml_serializers:
        if not tags_match(element.tag, xml_serializer.xml_element.tag):
            continue
        if not attributes_subset_of(xml_serializer.xml_element.attrib, element.attrib):
            continue
        return xml_serializer()
    raise UnsupportedElementException(lxml.etree.tostring(element, pretty_print=True))


# flexi.xml.matches decorators fill this list
tree_serializers = []


def get_tree_serializer(value):
    for tree_serializer in tree_serializers:
        if type(value) is tree_serializer.python_type:
            return tree_serializer()
    raise UnsupportedPythonTypeException(str(type(value)))
