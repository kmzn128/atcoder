N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
wa = 0
prev = 0
for i in range(N):
    wa += B[A[i]-1]
    if(prev == A[i]-2 and i > 1):
        wa += C[i-2]
    prev = A[i]-1
print(wa)
        