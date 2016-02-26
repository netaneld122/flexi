import unittest
import flexi


class TestJson(unittest.TestCase):

    @unittest.skip('XML serialization is not implemented yet')
    def test_sanity(self):
        input_xml = r'files\basic_data.xml'
        output_xml = r'files\output\basic_data.xml'
        root = flexi.xml.load(input_xml)
        flexi.xml.dump(root, output_xml)
        self.assertEqual(root, flexi.xml.load(output_xml))
