N, M, L = map(int, input().split())
towns = []
for i in range(M):
    towns.append(list(map(int, input().split())))
Q = int(input())
query = []
for i in range(Q):
    query.append(list(map(int, input().split())))
import collections
import heapq

def make_graph(li):
    dic = collections.defaultdict(collections.defaultdict)
    for town in towns:
        if(town[0] not in dic):
            dic.update({town[0]:{town[1]:town[2]}})
        else:
            dic[town[0]].update({town[1]:town[2]})
        if(town[1] not in dic):
            dic.update({town[1]:{town[0]:town[2]}})
        else:
            dic[town[1]].update({town[0]:town[2]})
    return dic        

def find_path(g,s,t):
    score = 0
    searching_heap = []
    checked = {start: score}
    heapq.heappush(searching_heap, (score, path))
    while(len(searching_heap) > 0):
        score, path = heapq.heappop(searching_heap)
        latest_pos = path[-1]
        if(latest_pos == goal):
            return path
        for next_pos, weight in g[latest_pos].items():
            new_path = path + [next_pos]
            new_score = score + weight
            if(next_pos in checked and checked[next_pos] <= new_score):
                continue
            else:
                checked[next_pos] = new_score
                heapq.heappush(searching_heap, (new_score, new_path))

 
g = make_graph(towns)
for q in query:
    path = find_path(g, q[0], q[1])
    
    
