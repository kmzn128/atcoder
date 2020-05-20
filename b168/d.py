N, M = map(int, input().split())
A = [0]*M
B = [0]*M
for i in range(M):
    A[i], B[i] = map(int, input().split())

from collections import deque
def bfs(graph, start_node, parent):
    next_nodes = deque([])
    seen_nodes = set()
    
    next_nodes.append(start_node)
    seen_nodes.add(start_node)
    parent[start_node] = 0
    while next_nodes:
        node = next_nodes.popleft()
#         if node == key:
#             return node
        if node in graph:
            for n in graph[node]:
                if not n in seen_nodes:
                    next_nodes.append(n)
                    seen_nodes.add(n)
                    parent[n] = node
    return

def Main(N, M, A, B):
    g = {}
    for i in range(M):
        if A[i] not in g:
            g[A[i]] = []
        if B[i] not in g:
            g[B[i]] = []
        g[A[i]].append(B[i])
        g[B[i]].append(A[i])
    parent = {}
    bfs(g, 1, parent)
    ans = []
    for i in range(2, N+1):
        ans.append(parent[i])
    return 'Yes', ans
          
                    
yn, out = Main(N, M, A, B)
print(yn)
for e in out:
    print(e)