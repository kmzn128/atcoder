N, M = map(int, input().split())
A = [0]*N
B = [0]*N
C = [0]*M
D = [0]*M
for i in range(N):
    A[i], B[i] = map(int, input().split())
for i in range(M):
    C[i], D[i] = map(int, input().split())
    
def Main(N, M, A, B, C, D):
    ans = []
    for i in range(N):
        min_dist = 10**9
        min_ind = 1
        for j in range(M):
            dist = abs(A[i]-C[j])+abs(B[i]-D[j])
            if min_dist > dist:
                min_dist = dist
                min_ind = j+1
        ans.append(min_ind)
    return ans
    
res = Main(N, M, A, B, C, D)
for e in res:
    print(e)
