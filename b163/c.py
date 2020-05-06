def Main(N, A):
    d = {}
    for i in range(1, N+1):
        d[i] = 0
    for e in A:
        d[e] += 1
    return d.values()

def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = Main(N, A)
    for e in out:
        print(e)

if __name__ == '__main__':
    main()