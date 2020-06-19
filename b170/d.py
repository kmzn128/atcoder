N = int(input())
A = list(map(int, input().split()))


from collections import Counter
def Main(N, A):
    A.sort()
    amax = A[-1]+1
    d = {}
    for i in range(1, amax):
        d[i] = 0
    for a in A:
        i = 1
        while a*i < amax:
            d[a*i] += 1
            i += 1
    ans = 0
    for a in A:
        if d[a] == 1:
            ans += 1
    return ans

print(Main(N, A))