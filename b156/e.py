class Mint:
    
    MOD = 10**9+7
    
    def __init__(self, x=0):
        self.x = (x%self.MOD + self.MOD) % self.MOD
    
    def __iadd__(self, other):
        self.x += other.x
        if self.x >= self.MOD:
            self.x -= self.MOD
        return self
    
    def __isub__(self, other):
        self.x += self.MOD - other.x
        if (self.x >= self.MOD):
            self.x -= self.MOD
        return self
    
    def __imul__(self, other):
        self.x *= other.x
        self.x %= self.MOD;
        return self;
    
    def __add__(self, other):
        ans = Mint(self.x)
        ans += other
        return ans
        
    def __sub__(self, other):
        ans = Mint(self.x)
        ans -= other
        return ans
    
    def __mul__(self, other):
        ans = Mint(self.x)
        ans *= other
        return ans
    
    def __pow__(self, n):
        if n == 0:
            return Mint(1)
        a = self.__pow__(n >> 1)
        a *= a
        if n&1:
            a *= self
        return a
    
    def inv(self):
        return self**(self.MOD-2)
    
    def __ifloordiv__(self, other):
        self *= other.inv()
        return self
    
    def __floordiv__(self, other):
        ans = Mint(self.x)
        ans //= other
        return ans
        
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
    
    def comb(self, n, k):
        assert self.n < Mint.MOD
        if k < 0 or k > self.n:
            return Mint(0)
        if k == 0 or k == self.n:
            return Mint(1)
        return self.fact[n]*self.ifact[k]*self.ifact[n-k]
    
        

def Main(N, K):
    ans = Mint(0)
    A = Comb2(N)
    for i in range(N):
        a = A.comb(N, i)
        b = A.comb(N-1, i)
        ans += a*b
        if i == K:
            return ans.x
    return ans.x

def main():
    N, K = list(map(int, input().split()))
    print(Main(N, K))

if __name__ == '__main__':
    main()