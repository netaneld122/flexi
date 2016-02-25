import unittest
import flexi


class TestTree(unittest.TestCase):

    def test_sanity(self):
        root = flexi.Tree()
        root.key.int = 1
        root.key.double = 2.0
        root.key.string = 'string'
