import math
import itertools
A, B = map(int, input().split())
def get_cds(a, b):
    low = min(a, b)
    high = max(a, b)
#     low_sqrt = math.sqrt(low)
#     high_sqrt = math.sqrt(high)
    i = 2
    candidates = []
    while(i <= low):
        if(low % i == 0):
            candidates.append(i)
        i += 1
    cds = []
    for j in candidates:
        if(high % j == 0):
            cds.append(j)
    cds2 = []
    while(len(cds) > 0):
        e = cds.pop(0)
        for ee in cds[:]:
            if(ee % e == 0):
                cds.remove(ee)
        cds2.append(e)
    return cds2

print(len(get_cds(A, B)) + 1)

