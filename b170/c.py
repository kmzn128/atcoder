X, N = map(int, input().split())
P = list(map(int, input().split()))

def Main(X, N, P):
    if N == 0:
        return X
    anss = []
    for i in range(102):
        if i in P:
            continue
        else:
            ab = 1000
            for e in P:
                ab = min(ab, abs(i-e))
            anss.append((i, ab))
    anss.sort(key = lambda x: x[1])
    ans = []
    mi = anss[0][1]
    for el in anss:
        if el[1] == mi:
            ell = (abs(X-el[0]), el[0])
            ans.append(ell)
        else:
            break
    ans.sort()
    return ans[0][1]
            
        
                    
out = Main(X, N, P)
print(out)