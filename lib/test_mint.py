import unittest
from mint import Mint

class TestMint(unittest.TestCase):
    
    MOD = 10**9+7
    TEN = 10**10
    
    def test_init(self):
        ans = Mint(self.TEN)
        self.assertEqual(self.TEN%self.MOD, ans.x)
    
    def test_iadd(self):
        ans = Mint(4)
        ans += Mint(4)
        self.assertEqual(8, ans.x)
        
    def test_iadd_2(self):
        ans = Mint(self.TEN)
        ans += Mint(self.TEN)
        exp = (self.TEN%self.MOD + self.TEN%self.MOD) % self.MOD
        self.assertEqual(exp, ans.x)
    
    def test_isub(self):
        ans = Mint(10)
        ans -= Mint(2)
        self.assertEqual(8, ans.x)
        
    def test_isub_2(self):
        ans = Mint(self.TEN*2)
        ans -= Mint(self.TEN)
        exp = self.TEN%self.MOD
        self.assertEqual(exp, ans.x)
    
    def test_imul(self): 
        ans = Mint(10)
        ans *= Mint(2)
        self.assertEqual(20, ans.x)
        
    def test_imul_2(self):
        ans = Mint(self.TEN)
        ans *= Mint(self.TEN)
        exp = (10**20)%self.MOD
        self.assertEqual(exp, ans.x)
        
    def test_add(self):
        a = Mint(2)
        b = Mint(2)
        ans = a + b
        self.assertEqual(4, ans.x)
        self.assertEqual(2, a.x)
        
    def test_add_2(self):
        a = Mint(self.TEN)
        b = Mint(self.TEN)
        ans = a + b
        exp = (self.TEN%self.MOD + self.TEN%self.MOD) % self.MOD
        self.assertEqual(exp, ans.x) 

    def test_sub(self):
        a = Mint(4)
        b = Mint(2)
        ans = a - b
        self.assertEqual(2, ans.x)
        
    def test_sub_2(self):
        a = Mint(self.TEN*2)
        b = Mint(self.TEN)
        ans = a - b
        exp = self.TEN % self.MOD
        self.assertEqual(exp, ans.x) 

    def test_mul(self):
        a = Mint(4)
        b = Mint(2)
        ans = a * b
        self.assertEqual(8, ans.x)
        
    def test_mul_2(self):
        a = Mint(self.TEN)
        b = Mint(self.TEN)
        ans = a * b
        exp = 10**20 % self.MOD
        self.assertEqual(exp, ans.x)
        
    def test_pow(self):
        a = Mint(2)
        n = 10
        ans = a**n
        self.assertEqual(2**10, ans.x)
    
    def test_pow_2(self):
        a = Mint(self.TEN)
        n = 2
        ans = a**n
        exp = 10**20 % self.MOD
        self.assertEqual(exp, ans.x)
    
    def test_idiv(self):
        ans = Mint(10)
        ans //= Mint(2)
        self.assertEqual(5, ans.x)
         
    def test_idiv_2(self):
        ans = Mint(self.TEN)
        ans //= Mint(2)
        self.assertEqual((self.TEN//2)%self.MOD, ans.x)
    
    def test_div(self):
        a = Mint(4)
        b = Mint(2)
        ans = a // b
        self.assertEqual(2, ans.x)
        
    def test_div_2(self):
        a = Mint(self.TEN*2)
        b = Mint(self.TEN)
        ans = a // b
        self.assertEqual(2, ans.x)           
      
if __name__ == "__main__":
    unittest.main()    