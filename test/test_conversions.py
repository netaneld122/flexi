import unittest
import flexi


class TestXml(unittest.TestCase):

    input_xml = r'files\basic_data.xml'
    input_json = r'files\basic_data.json'
    output_xml = r'files\output\basic_data.xml'
    output_json = r'files\output\basic_data.json'

    def test_xml_to_json(self):
        root1 = flexi.xml.load(self.input_xml)
        flexi.json.dump(root1, self.output_json)
        root2 = flexi.json.load(self.output_json)
        self.assertEqual(root1, root2)
