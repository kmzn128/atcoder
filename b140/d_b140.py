N, K = map(int, input().split())
S = str(input())

def main(N,K,S):
    d1 = [1]
    d2 = []
    flip = True
    for i in range(1, N):
        if S[i] == S[i-1]:
            if flip:
                d1[-1] += 1
            else:
                d2[-1] += 1
        else:
            if flip:
                d2.append(1)
                flip = False
            else:
                d1.append(1)
                flip = True
    if len(d1) == 1 and len(d2) <= 1:
        return N-1
    d1.reverse()
    d2.reverse()
    for i in range(K):
        if len(d1) <= 1 or len(d2) == 0:
            break
        p1 = d1.pop()
        p2 = d1.pop()
        p3 = d2.pop()
        d1.append(p1+p2+p3)
    if len(d1) == 1 and len(d2) <= 1:
        return N-1
    return sum(d1) - len(d1) + sum(d2) - len(d2)
    
    
print(main(N,K,S))