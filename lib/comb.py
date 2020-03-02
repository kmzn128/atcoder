from mint import Mint

class Comb:
    
    def __init__(self):
        pass
    
    def comb(self, n, k):
        assert n < Mint.MOD
        if k < 0 or k > n:
            return Mint(0)
        if k == 0 or k == n:
            return Mint(1)
        numerator = Mint(n-k+1)
        for i in range(n-k+2, n+1):
            numerator *= Mint(i)
        d = Mint(1)
        for i in range(2, k+1):
            d *= Mint(i)
        denominator = d.inv()
        return numerator*denominator