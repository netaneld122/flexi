import unittest
import flexi


class TestJson(unittest.TestCase):

    def test_sanity(self):
        input_json = r'files\basic_data.json'
        output_json = r'files\output\basic_data.json'
        root = flexi.json.load(input_json)
        flexi.json.dump(root, output_json)
        self.assertEqual(root, flexi.json.load(output_json))
