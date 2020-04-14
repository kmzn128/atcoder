def Main(N, M, S, C):
    digits = {1:set([]), 2:set([]), 3:set([])}
    for i in range(M):
        digits[S[i]].add(C[i])
    for k, v in digits.items():
        if len(v) >= 2:
            return -1
        
                

def main():
    N, M = map(int, input().split())
    S = [0]*M
    C = [0]*M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    print(Main(N, M, S, C))

if __name__ == '__main__':
    main()