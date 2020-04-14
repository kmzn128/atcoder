import numpy as np
def Main(N, S):
    num = [0]*3
    for c in S:
        if c == 'R':
            num[0] += 1
        elif c == 'G':
            num[1] += 1
        else:
            num[2] += 1
    ans = np.prod(num)
    sub = 0
    i = 0
    j = 1
    while(i-2 < N):
        while(i+2*j < N):
            a = i
            b = i+j
            c = i+2*j
            if S[a] != S[b] and S[a] != S[c] and S[b] != S[c]:
                sub += 1
            j += 1
        i += 1
        j = 1
    return ans - sub
        
    

def main():
    N = int(input())
    S = str(input())
    print(Main(N,S))

if __name__ == '__main__':
    main()