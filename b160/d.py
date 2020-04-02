from itertools import combinations
def Main(N, X, Y):
    ar = range(N)
    X -= 1
    Y -= 1
    comb = combinations(ar, 2)
    ans = {i:0 for i in range(N-1)}
    for i, j in comb:
        dist = 0
        if i <= X and Y <= j:
            dist = X - i + j - Y + 1
        elif i > X and Y <= j:
            dist = min(i-X + 1 + j-Y, j-i)
        elif i <= X and Y > j:
            dist = min(X-i + 1 + Y-j, j-i)
        else:
            dist = min(i-X + 1 + Y-j, j-i)
        ans[dist-1] += 1
    return ans.values()

def main():
    N, X, Y = map(int, input().split())
    out = Main(N, X, Y)
    for e in out:
        print(e)

if __name__ == '__main__':
    main()