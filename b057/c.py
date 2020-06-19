N = int(input())

def Main(N):
    ans = 10
    i = 1
    while i*i <= N:
        if N%i == 0:
            ans = min(ans, max(len(str(i)), len(str(N//i))))
        i += 1
    return ans
    
print(Main(N))
