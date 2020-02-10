import sys
input = sys.stdin.readline

def Main(N, V):
    dp = [[0 for _ in range(3)] for _ in range(N+1)]
    for i in range(N):
        for j in range(3):
            for k in range(3):
                if(j != k):
                    dp[i+1][j] = max(dp[i+1][j], dp[i][k] + V[i][j])
    return max(dp[N])

def main():
    N = int(input())
    V = []
    for i in range(N):
        V.append(list(map(int, input().split())))
    print(Main(N, V))

if __name__ == '__main__':
    main()