def Main(N, A):
    ans = [0]*N
    hist = [0]*N
    for i in range(N):
        hist[A[i]-1] += 1
    whole = 0
    for i in range(N):
        whole += hist[i]*(hist[i]-1)//2
    for i in range(N):
        ans[i] = whole - hist[A[i]-1] + 1
    return ans

def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = Main(N, A)
    for e in out:
        print(e)

if __name__ == '__main__':
    main()