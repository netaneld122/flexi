from flexi.xml import matches
from flexi.xml import serializer_registry
from flexi.xml import element_maker

from flexi.tree import Tree
from flexi.list_tree import ListTree
from flexi.root_tree import RootTree


def tree_children_to_element(tree, element):
    for key in tree:
        serializer = serializer_registry.get_tree_serializer(tree[key])
        serializer.tree_to_xml(key, tree[key], element)


def element_children_to_tree(element, tree):
    for sub_element in element.iterchildren():
        serializer = serializer_registry.get_xml_serializer(sub_element)
        serializer.xml_to_tree(sub_element, tree)


class ContainerSerializer(object):

    def tree_to_xml(self, name, tree, element):
        # Create sub element
        sub_element = element_maker.make(self.xml_element.tag, name=name)
        element.append(sub_element)
        tree_children_to_element(tree, sub_element)
        return element

    def xml_to_tree(self, element, tree):
        # Create sub tree
        key = element.get('name')
        tree[key] = self.python_type()
        element_children_to_tree(element, tree[key])
        return tree


@matches.xml_element('root')
@matches.python_type(RootTree)
class RootTreeSerializer(ContainerSerializer):

    def tree_to_xml(self, name, tree, element=None):
        # Create a new root element
        element = element_maker.make(self.xml_element.tag)
        tree_children_to_element(tree, element)
        return element

    def xml_to_tree(self, element, tree=None):
        # Create a new RootTree
        tree = self.python_type()
        element_children_to_tree(element, tree)
        return tree


@matches.xml_element('tree')
@matches.python_type(Tree)
class TreeSerializer(ContainerSerializer):
    pass


@matches.xml_element('list')
@matches.python_type(ListTree)
class ListSerializer(ContainerSerializer):
    pass

