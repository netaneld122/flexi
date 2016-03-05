from flexi.xml import matches
from flexi.xml import serializer_registry
from flexi.xml import element_maker

from flexi.tree import Tree
from flexi.tree import RootTree


class ContainerSerializer(object):
    pass


@matches.xml_element('tree')
@matches.python_type(Tree)
class TreeSerializer(ContainerSerializer):

    @staticmethod
    def tree_children_to_element(tree, element):
        for key in tree:
            serializer = serializer_registry.get_tree_serializer(tree[key])
            serializer.tree_to_xml(key, tree[key], element)

    @staticmethod
    def element_children_to_tree(element, tree):
        for sub_element in element.iterchildren():
            serializer = serializer_registry.get_xml_serializer(sub_element)
            serializer.xml_to_tree(sub_element, tree)

    def tree_to_xml(self, name, tree, element):
        # Create sub element
        sub_element = element_maker.make(self.xml_element.tag, name=name)
        element.append(sub_element)
        self.tree_children_to_element(tree, sub_element)
        return element

    def xml_to_tree(self, element, tree):
        # Create sub tree
        key = element.get('name')
        tree[key] = self.python_type()
        self.element_children_to_tree(element, tree[key])
        return tree


class Element(Tree):
    pass


@matches.xml_element('element')
@matches.python_type(Element)
class ElementSerializer(TreeSerializer):
    pass


@matches.xml_element('root')
@matches.python_type(RootTree)
class RootTreeSerializer(TreeSerializer):

    def tree_to_xml(self, name, tree, element=None):
        root_element = element_maker.make('root')
        self.tree_children_to_element(tree, root_element)
        return root_element

    def xml_to_tree(self, element, tree=None):
        tree = RootTree()
        self.element_children_to_tree(element, tree)
        return tree


@matches.xml_element('list')
@matches.python_type(list)
class ListSerializer(ContainerSerializer):

    @staticmethod
    def tree_to_xml(name, list_instance, element):
        # Create list element
        list_element = element_maker.make('list', name=name)
        element.append(list_element)
        # Add elements to the list element
        for tree in list_instance:
            list_sub_element = element_maker.make('element')
            list_element.append(list_sub_element)
            for key in tree:
                serializer = serializer_registry.get_tree_serializer(tree[key])
                serializer.tree_to_xml(key, tree[key], list_sub_element)
        return element

    @staticmethod
    def xml_to_tree(list_element, tree):
        # Create sub tree
        key = list_element.get('name')
        tree[key] = list()
        for list_sub_element in list_element.iterchildren():
            list_item = Tree()
            tree[key].append(list_item)
            for sub_element_child in list_sub_element.iterchildren():
                serializer = serializer_registry.get_xml_serializer(sub_element_child)
                serializer.xml_to_tree(sub_element_child, list_item)
        return tree
