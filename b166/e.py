def Main(N, A):
    d = {}
    d2 = {}
    ans = 0
    for i in range(N):
        p = i+A[i]
        if p not in d:
            d[p] = []
        d[p].append(i)
    for i in range(N):
        q = i-A[i]
        if q not in d2:
            d2[q] = []
        d2[q].append(i)
    for k, v in d.items():
        if len(v) > 0 and k in d2:
            ans += len(v) * len(d2[k])
    return ans
        
    
def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(Main(N, A))

if __name__ == '__main__':
    main()