N = int(input())
d = list(map(int, input().split()))
import itertools
combi = itertools.combinations(d, 2)
wa = 0
for e in combi:
    wa += e[0]*e[1]
print(wa)