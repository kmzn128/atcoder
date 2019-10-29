N = int(input())
P = list(map(int, input().split()))
X = [[0 for i in range(N)] for j in range(N)]
def max_second(li):
    if(len(li) == 1):
        return li[0], li[0]
    l = li[:]
    mxv = max(l)
    l.remove(mxv)
    return mxv, max(l)

for i in range(N-1):
    for j in range(i+1, N):
        first, second = max_second(P[i:j])
        if(first == second):
            X[i][j] = min(first, P[j])
        elif(first < P[j]):
            X[i][j] = first
        elif(first > P[j] and second < P[j]):
            X[i][j] = P[j]
        elif(second > P[j]):
            X[i][j] = second
print(sum([sum(row) for row in X]))
