import unittest
from comb import Comb
from mint import Mint

class TestComb(unittest.TestCase):
    
    def test_comb(self):
        exp = Mint(6)
        ans = Comb().comb(4, 2)
        self.assertEqual(exp.x, ans.x)