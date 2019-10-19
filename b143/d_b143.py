N = int(input())
L = list(map(int, input().split()))
L.sort()
wa = 0
import bisect
for i in range(N-1,1,-1):
    for j in range(i-1,0,-1):
        diff = L[i]-L[j]
        k = bisect.bisect_right(L, diff)
        wa += j-k if j-k > 0 else 0           
             
print(wa)