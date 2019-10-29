N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
wa = 0
for i in range(N):
    wa += B[A[i]-1]
    if(i > 0 and A[i]-A[i-1] == 1):
        wa += C[A[i-1]-1]
print(wa)
        