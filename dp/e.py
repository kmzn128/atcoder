import sys
input = sys.stdin.readline

def Main(N, W, V):
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if(j < V[i][0]):
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-V[i][0]]+V[i][1])
    res = 0
    for j in range(W+1):
        if(dp[N][j] <= W):
            res = j
        else:
            break
    return res            

def main():
    N, W = map(int, input().split())
    V = []
    for _ in range(N):
        V.append(list(map(int, input().split())))
    print(Main(N, W, V))

if __name__ == '__main__':
    main()