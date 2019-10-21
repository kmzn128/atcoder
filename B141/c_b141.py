N, K, Q = map(int, input().split())
A = []
for i in range(Q):
    A.append(int(input()))
score = [0]*N
init_score = [K]*N
for i in A:
    score[i-1] += 1
final_score = [init_score[i]-Q+score[i] for i in range(N)]
for i in final_score:
    print("Yes") if i > 0 else print("No")