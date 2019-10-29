N = int(input())
B = list(map(int, input().split()))
def c(n, b):
    A = [0 for i in range(n)]
    for i in range(n):
        if(i == 0 or i == 1):
            A[i] = b[0]
        else:
            A[i] = b[i-1]
            if(b[i-1] < b[i-2]):
                A[i-1] = b[i-1]
    return sum(A)
print(c(N,B))