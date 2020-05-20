
N, A, B = map(int, input().split())
X = list(map(int, input().split()))

def Main(N):
    ans = 0
    for i in range(1, N):
        di = X[i]-X[i-1]
        ans += min(di*A, B)
    return ans
          
print(Main(N))