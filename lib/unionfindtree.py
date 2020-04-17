class UnionFindTree:
    
    def __init__(self, n):
        if n == 0:
            raise Exception("n is more than 1")
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
        self.num = {}
        for i in range(n):
            self.num.update({i:1})
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.num[y] += self.num[x]
            del self.num[x]
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.num[x] += self.num[y]
            del self.num[y]
        
    
    def same(self, x, y):
        X = self.find(x)
        Y = self.find(y)
        return X == Y