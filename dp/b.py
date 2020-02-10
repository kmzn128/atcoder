import sys
input = sys.stdin.readline

def Main(N, K, h):
    dp =[float('inf')]*N
    dp[0] = 0
    for i in range(N):
        for j in range(1, min(N-i,K+1)):
            dp[i+j] = min(dp[i+j], dp[i] + abs(h[i] - h[i+j]))
    return dp[N-1]

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    print(Main(N, K, h))

if __name__ == '__main__':
    main()