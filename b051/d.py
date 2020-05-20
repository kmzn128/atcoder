N, M = map(int, input().split())
A = [0]*M
B = [0]*M
C = [0]*M
for i in range(M):
    A[i], B[i], C[i] = map(int, input().split())

import heapq

def dijkstra(graph, start, goal):
    path = [start]
    score = 0
    searching_heap = []
    checked = {start: score}
    heapq.heappush(searching_heap, (score, path))
    while(len(searching_heap) > 0):
        score, path = heapq.heappop(searching_heap)
        latest_pos = path[-1]
        if(latest_pos == goal):
            return path, score
        for next_pos, weight in graph[latest_pos].items():
            new_path = path + [next_pos]
            new_score = score + weight
            if(next_pos in checked and checked[next_pos] <= new_score):
                continue
            else:
                checked[next_pos] = new_score
                heapq.heappush(searching_heap, (new_score, new_path)) 
import copy

def Main(N, M, A, B, C):
    g = {}
    for i in range(M):
        if A[i] not in g:
            g[A[i]] = {}
        if B[i] not in g:
            g[B[i]] = {}
        g[A[i]].update({B[i]:C[i]})
        g[B[i]].update({A[i]:C[i]})
    ans = 0
    for i in range(1, N):
        for j in range(i+1, N+1):
            path, score = dijkstra(g, i, j)
            if len(path) > 2:
                if i in g and j in g[i] and score < g[i][j]:
                    ans += 1
    return ans
                
          
                    
print(Main(N, M, A, B, C))