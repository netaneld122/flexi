import unittest
import flexi


class TestXml(unittest.TestCase):

    @staticmethod
    def uglify(xml_content):
        bad_chars = '\n\r\t '
        for bad_char in bad_chars:
            xml_content = xml_content.replace(bad_char, '')
        return xml_content.strip()

    input_xml = r'files\basic_data.xml'
    output_xml = r'files\output\basic_data.xml'

    def test_tree_equality(self):
        root = flexi.xml.load(self.input_xml)
        flexi.xml.dump(root, self.output_xml)
        self.assertEqual(root, flexi.xml.load(self.output_xml))

    # @TODO Add list serialization tests
