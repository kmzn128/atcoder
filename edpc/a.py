def Main(N, H):
    dp = [0]*N
    dp[1] = abs(H[0]-H[1])
    for i in range(2, N):
        dp[i] = min(abs(H[i]-H[i-1])+dp[i-1], abs(H[i]-H[i-2])+dp[i-2])
    return dp[N-1]

def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(Main(N, H))

if __name__ == '__main__':
    main()