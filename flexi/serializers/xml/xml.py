import lxml.objectify
import lxml.etree

import flexi.serializers.xml.recursive_copy as recursive_copy

from flexi.tree import Tree


def load(xml_file_path):
    with open(xml_file_path) as fp:
        xml = lxml.objectify.parse(fp)
        return recursive_copy.xml_to_tree(xml.getroot(), Tree())

# @TODO Consider using lxml.etree.fromstring and lxml.etree.tostring instead of lxml.objectify.E
# @TODO because that way remove_objectify_garbage won't be needed


def remove_objectify_garbage(root_element):
    lxml.etree.strip_attributes(root_element, '{http://codespeak.net/lxml/objectify/pytype}pytype')
    lxml.etree.strip_attributes(root_element, '{http://www.w3.org/2001/XMLSchema-instance}nil')
    lxml.etree.cleanup_namespaces(root_element)


def dump(tree, xml_file_path):
    root_element = lxml.objectify.E.root()
    recursive_copy.tree_to_xml(tree, root_element)
    remove_objectify_garbage(root_element)
    root_tree = root_element.getroottree()
    with open(xml_file_path, 'w') as fp:
        root_tree.write(fp, pretty_print=True)
