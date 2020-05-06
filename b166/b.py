def Main(N, K, d, A):
    se = set()
    for a in A:
        se.update(a)
    return N - len(se)
        
def main():
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    print(Main(N, K, d, A))

if __name__ == '__main__':
    main()