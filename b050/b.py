N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = [0]*M
X = [0]*M
for i in range(M):
    P[i], X[i] = map(int, input().split())

def Main(N, T, M, P, X):
    ans = [0]*M
    for i in range(M):
        TT = T.copy()
        TT[P[i]-1] = X[i]
        ans[i] = sum(TT)
    return ans

res = Main(N, T, M, P, X)
for e in res:
    print(e)