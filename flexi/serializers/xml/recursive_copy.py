import lxml.objectify

from flexi.tree import Tree
from flexi.serializers.xml.param_serializers import get_param_serializer
from flexi.serializers.xml.param_serializers import get_leaf_serializer
from flexi.serializers.xml.exceptions import UnsupportedElementException


# @TODO Support lists and queues


def xml_to_tree(element, tree):

    if 'tree' == element.tag:
        tree = tree.create(element.get('name'))

    if element.tag in ('root', 'tree'):
        for sub_element in element.iterchildren():
            xml_to_tree(sub_element, tree)
    elif 'param' == element.tag:
        serializer = get_param_serializer(element.get('type'))
        serializer.serialize_param_into_leaf(element, tree)
    else:
        raise UnsupportedElementException(element.tag)

    return tree


def tree_to_xml(tree, element):

    for key in tree:
        if isinstance(tree[key], Tree):
            param_element = lxml.objectify.E.tree(name=key)
            element.append(param_element)
            tree_to_xml(tree[key], param_element)
        else:
            serializer = get_leaf_serializer(type(tree[key]))
            serializer.serialize_leaf_into_param(key, tree[key], element)

    return element
