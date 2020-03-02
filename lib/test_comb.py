import unittest
from comb import Comb
from mint import Mint
from comb2 import Comb2

class TestComb(unittest.TestCase):
    
    def test_comb(self):
        exp = [0, 1, 4, 6, 4, 1, 0]
        ans = [Comb().comb(4, i) for i in range(-1, 6)]
        for e, a in zip(exp, ans):
            self.assertEqual(e, a.x)

    def test_comb2(self):
        exp = [0, 1, 4, 6, 4, 1, 0]
        c = Comb2(4)
        ans = [c.comb(i) for i in range(-1, 6)]
        for e, a in zip(exp, ans):
            self.assertEqual(e, a.x)        