import heapq
N, M = map(int, input().split())
A = list(map(int, input().split()))
AA = [[-x, x] for x in A]
heapq.heapify(AA)
for i in range(M):
    x, y = heapq.heappop(AA)
    heapq.heappush(AA, [-(y//2), y//2])
AAA = [x[1] for x in AA]
print(sum(AAA))
    