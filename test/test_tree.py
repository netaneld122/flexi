import unittest

from flexi.tree import Tree
from flexi.tree import create_sub_tree


class TestTree(unittest.TestCase):

    def test_list(self):
        root = Tree()
        create_sub_tree(root, 'tree').list = [1, 2, 3]
        self.assertListEqual(root.tree.list, [1, 2, 3])

    def test_get_item(self):
        root = Tree()
        create_sub_tree(root, 'tree').int = 1
        self.assertEqual(root.tree['int'], 1)

    def test_recursive_scanning(self):
        root = Tree()
        create_sub_tree(root, 'tree')
        root.tree.int = 1
        root.tree.double = 2.0
        root.tree.string = 'string'
        create_sub_tree(root.tree, 'tree2').list = [1, 2, 3]

        def recurse(tree):
            for key in tree:
                if isinstance(tree[key], Tree):
                    recurse(tree[key])
        recurse(root)

    def test_contains(self):
        root = Tree()
        create_sub_tree(root, 'tree').string = 'string'
        self.assertIn('string', root.tree)

    def test_representation(self):
        root = Tree()
        create_sub_tree(create_sub_tree(root, 'a'), 'b').c = 0
        self.assertSequenceEqual(str(root), "{'a': {'b': {'c': 0}}}")

    def test_equality(self):
        root1 = Tree()
        create_sub_tree(create_sub_tree(root1, 'a'), 'b').c = 2
        root2 = Tree()
        create_sub_tree(create_sub_tree(root2, 'a'), 'b').c = 2
        self.assertEqual(root1, root2)

        root2.a.b.c = 3
        self.assertNotEqual(root1, root2)

    def test_multiple_sub_tree_creation(self):
        root = Tree()
        create_sub_tree(root, 'a.b.c.d')
        root.a.b.c.d.value = 1
