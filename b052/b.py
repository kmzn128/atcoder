N = int(input())
S = str(input())

def Main(N, S):
    ans = 0
    mx = ans
    for c in S:
        if c == "I":
            ans += 1
        else:
            ans -= 1
        mx = max(mx, ans)
    return mx
        
res = Main(N, S)
print(res)