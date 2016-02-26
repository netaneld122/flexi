import unittest
import flexi


class TestTree(unittest.TestCase):

    def test_list(self):
        root = flexi.Tree()
        root.tree.tree2.list = [1, 2, 3]
        self.assertListEqual(root.tree.tree2.list, [1, 2, 3])

    def test_get_item(self):
        root = flexi.Tree()
        root.tree.int = 1
        self.assertEqual(root.tree['int'], 1)

    def test_recursive_scanning(self):
        root = flexi.Tree()
        root.tree.int = 1
        root.tree.double = 2.0
        root.tree.string = 'string'
        root.tree.tree2.list = [1, 2, 3]

        def recurse(tree):
            for key in tree:
                if isinstance(tree[key], flexi.Tree):
                    recurse(tree[key])
        recurse(root)

    def test_contains(self):
        root = flexi.Tree()
        root.tree.string = 'string'
        self.assertIn('string', root.tree)
