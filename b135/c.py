def Main(N, A, B):
    ans = 0
    remain = 0
    for i in range(N):
        if A[i] >= B[i]:
            ans += B[i]
        else: # A[i] < B[i]
            ans += A[i]
            remain = B[i]-A[i]
            next_attack = A[i+1]-remain
            if next_attack > 0:
                ans += remain
                A[i+1] -= remain
            else:
                ans += A[i+1]
                A[i+1] = 0
    return ans
        

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(Main(N, A, B))


if __name__ == '__main__':
    main()
