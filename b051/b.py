K, S = map(int, input().split())

def Main(K, S):
    ans = 0
    for i in range(K+1):
        for j in range(K+1):
            if 0 <= S-i-j <= K:
                ans += 1
    return ans
        
res = Main(K, S)
print(res)