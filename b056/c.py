X = int(input())

def Main(X):
    if X <= 2:
        return X
    ans = 0
    for i in range(1, X):
        ans += i
        if ans >= X:
            return i
    
print(Main(X))
