from mint import Mint

class Comb2:
    
    def __init__(self, n):
        self.n = n
        self.fact = [Mint(1)]*(n+1)
        self.ifact = [Mint(1)]*(n+1)
        for i in range(1, n+1):
            self.fact[i] = self.fact[i-1]*Mint(i)
        self.ifact[n] = self.fact[n].inv()
        for i in range(n, 0, -1):
            self.ifact[i-1] = self.ifact[i]*Mint(i)
    
    def comb(self, k):
        assert self.n < Mint.MOD
        if k < 0 or k > self.n:
            return Mint(0)
        if k == 0 or k == self.n:
            return Mint(1)
        return self.fact[self.n]*self.ifact[k]*self.ifact[self.n-k]
    