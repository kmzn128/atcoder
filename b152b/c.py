def Main(N, P):
    ans = 1
    mi = P[0]
    for i in range(1, N):
        if mi > P[i]:
            ans += 1
            mi = P[i]
    return ans

def main():
    N = int(input())
    P = list(map(int, input().split()))
    print(Main(N, P))

if __name__ == '__main__':
    main()