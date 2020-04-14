def gcd(a, b):
    return gcd(b, a%b) if b != 0 else a

def Main(N):
    ans = 0
    memo2 = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if memo2[i][j] == 0:
                memo2[i][j] = gcd(i,j)
            for k in range(1, N+1):
                M = memo2[i][j]
                if memo2[M][k] == 0:
                    memo2[M][k] = gcd(M, k)
                ans += memo2[M][k]
    return ans
    

def main():
    N = int(input())
    print(Main(N))

if __name__ == '__main__':
    main()