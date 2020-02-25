from bisect import bisect_left
 
def lis(A: list):
    L = [A[0]]
    for a in A[1:]:
        if a > L[-1]:
            L.append(a)
        else:
            L[bisect_left(L, a)] = a
    return len(L)
 

lis([4,2,3,1,5])