N = int(input())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i], B[i] = map(int, input().split())

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

from collections import Counter      

def Main(N, A, B):
    a_cou = Counter(A)
    ans = 0
    for k, v in a_cou.items():
        ans += v*(v-1)//2
    ab = [0]*N
    for i in range(N):
        ab[i] = A[i]*B[i]
    ab_cou = Counter(ab)
    for k, v in ab_cou.items():
        if k == 0:
            ans += v*(v-1)//2
        elif -k in ab_cou:
            ans += ab_cou[k]*ab_cou[-k]
    return ans+N
    
print(Main(N, A, B))