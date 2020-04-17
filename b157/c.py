def Main(N, M, S, C):
    d = {1:set([]), 2:set([]), 3:set([])}
    for i in range(M):
        d[S[i]].add(C[i])
    for v in d.values():
        if len(v) >= 2:
            return -1
    if N == 3:
        d1 = d2 = d3 = 0
        if len(d[1]) == 0:
            d1 = 1
        else:
            d1 = d[1].pop()
            if d1 == 0:
                return -1
        if len(d[2]) == 0:
            d2 = 0
        else:
            d2 = d[2].pop()
        if len(d[3]) == 0:
            d3 = 0
        else:
            d3 = d[3].pop()
        return d1*100+d2*10+d3
    elif N == 2:
        d1 = d2 = 0
        if len(d[1]) == 0:
            d1 = 1
        else:
            d1 = d[1].pop()
            if d1 == 0:
                return -1
        if len(d[2]) == 0:
            d2 = 0
        else:
            d2 = d[2].pop()
        return d1*10+d2
    else:
        return d[1].pop()
            
            
    
                

def main():
    N, M = map(int, input().split())
    if M == 0:
        if N == 3:
            print(100)
        if N == 2:
            print(10)
        if N == 1:
            print(0)
        return
    S = [0]*M
    C = [0]*M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    print(Main(N, M, S, C))

if __name__ == '__main__':
    main()