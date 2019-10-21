il = input().split(' ')
N = int(il[0])
M = int(il[1])
A = []
B = []
for i in range(M):
    l = input().split(' ')
    A.append(int(l[0]))
    B.append(int(l[1]))

from collections import defaultdict
from collections import deque

dic = defaultdict(list)
for i in range(M):
    dic[A[i]].append(B[i])

def myprint(li):
    print(len(li))
    for i in range(len(li)):
        print(li[i])
            
for key in dic:
    path = []
    deq = deque([])
    path.append(key)
    deq.append((key,path))
    while(len(deq) > 0):
        node, path = deq.popleft()
        if(node not in dic):
            continue
        for e in dic[node]:
            new_path = path + [e]
            if(new_path[0] == e):
                myprint(new_path[:-1])
                exit()
            if(e in path):
                continue
            deq.append((e, new_path))
print("-1")