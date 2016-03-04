import lxml.objectify
import lxml.etree

import flexi.xml.serializers

from flexi.tree import Tree
from flexi.xml import element_maker
from flexi.xml import serializer_registry


flexi.xml.serializers.import_all()


def load(xml_file_path):
    with open(xml_file_path) as fp:
        xml = lxml.objectify.parse(fp)
        serializer = serializer_registry.get_xml_serializer(xml.getroot())
        return serializer.xml_to_tree(xml.getroot())


def dump(tree, xml_file_path):
    serializer = serializer_registry.get_tree_serializer(tree)
    element = serializer.tree_to_xml('root', tree)
    root_tree = element.getroottree()
    with open(xml_file_path, 'w') as fp:
        root_tree.write(fp, pretty_print=True)
