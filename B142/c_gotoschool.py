N = int(input())
people = list(map(int, input().split()))
out_list = [0]*N
for i in range(N):
    out_list[people[i]-1] = i + 1
print(" ".join(map(str, out_list)))