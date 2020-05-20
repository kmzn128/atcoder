N, Q = map(int, input().split())
a = []
b = []
for i in range(N-1):
    aa, bb = map(int, input().split())
    a.append(aa)
    b.append(bb)
p = []
x = []
for i in range(Q):
    pp, xx = map(int, input().split())
    p.append(pp)
    x.append(xx)
    

def Main(N, Q, a, b, p, x):
    ans = [0]*N
    for i in range(Q):
        ans[p[i]-1] += x[i]
    for i in range(N-1):
        ans[b[i]-1] += ans[a[i]-1]
    return ans
        
         

out = Main(N, Q, a, b, p, x)
print(" ".join(map(str, out)))