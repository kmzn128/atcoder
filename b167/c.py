from itertools import combinations

def Main(N, M, X, C, A):
    inds = list(range(N))
    ind_subset = []
    for i in range(1, N+1):
        for c in combinations(inds, i):
            ind_subset.append(c)
    ans = []
    for e in ind_subset:
        c = 0
        a = [0]*M
        for j in e:
            c += C[j]
            a = [a[k]+A[j][k] for k in range(M)]
        if min(a) >= X:
            ans.append(c)
    if len(ans) == 0:
        return -1
    else:
        return min(ans)      
    
def main():
    N, M, X = map(int, input().split())
    B = []
    C = []
    A = []
    for i in range(N):
        B = list(map(int, input().split()))
        c = B[0]
        a = B[1:]
        C.append(c)
        A.append(a)
    print(Main(N, M, X, C, A))

if __name__ == '__main__':
    main()