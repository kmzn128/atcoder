def Main(N, K, H):
    H.sort()
    if N <= K:
        return 0
    else:
        return sum(H[:N-K])

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    print(Main(N, K, H))

if __name__ == '__main__':
    main()