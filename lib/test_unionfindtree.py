import unittest
from unionfindtree import UnionFindTree

class TestUnionFindTree(unittest.TestCase):
    
    def test_init_exception(self):
        self.assertRaises(Exception, lambda: UnionFindTree(0))
    
    def test_init_1(self):
        uft = UnionFindTree(3)
        self.assertListEqual([0,1,2], uft.parent)
        self.assertListEqual([0]*3, uft.rank)
    
    def test_unite_1(self):
        uft = UnionFindTree(3)
        uft.unite(0,1)
        self.assertListEqual([0,0,2], uft.parent)
        self.assertListEqual([1,0,0], uft.rank)
    
    def test_find_1(self):
        uft = UnionFindTree(3)
        uft.unite(0,1)
        self.assertEqual(0, uft.find(0))
        self.assertEqual(0, uft.find(1))
    
    def test_same_1(self):
        uft = UnionFindTree(3)
        uft.unite(0,1)
        self.assertEqual(True, uft.same(0,1))
        self.assertEqual(False, uft.same(0,2))       