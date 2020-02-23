def Main(N, X):
    av = round(sum(X)/N)
    ans = 0
    for i in range(N):
        ans += (X[i]-av)**2
    return ans

def main():
    N = int(input())
    X = list(map(int, input().split()))
    print(Main(N, X))

if __name__ == '__main__':
    main()