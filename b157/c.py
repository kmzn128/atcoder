def Main(N, M, S, C):
    dig = [set([]),set([]),set([])]
    for i in range(M):
        dig[S[i]-1].add(C[i])
    for s in dig:
        if len(s) == 2:
            return -1
    if N == 3:
        if len(dig[0]) > 0 and list(dig[0])[0] == 0:
            return -1
        if len(dig[0]) == 0:
            dig[0].add(1)
        if len(dig[1]) == 0:
            dig[1].add(0)
        if len(dig[2]) == 0:
            dig[2].add(0)
        return list(dig[0])[0]*100+list(dig[1])[0]*10+list(dig[2])[0]
    elif N == 2:
        if len(dig[0]) > 0 and list(dig[0])[0] == 0:
            return -1
        if len(dig[0]) == 0:
            dig[0].add(1)
        if len(dig[1]) == 0:
            dig[1].add(0)
        return list(dig[0])[0]*10+list(dig[1])[0]
    else:
        return list(dig[0])[0]       
        
                

def main():
    N, M = map(int, input().split())
    if M == 0:
        if(N == 3):
            print(100)
        elif(N == 2):
            print(10)
        else:
            print(0)
        exit()
    S = [1]*M
    C = [0]*M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    print(Main(N, M, S, C))

if __name__ == '__main__':
    main()