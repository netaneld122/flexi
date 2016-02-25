import unittest
import flexi


class TestJson(unittest.TestCase):

    def test_sanity(self):
        root = flexi.json.load(r'files\basic_data.json')
        flexi.json.dump(root, r'files\output\basic_data.json')
