def Main(A, N, B):
    BINGO = (
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
        )
    ans_ind = []
    for e in B:
        if e in A:
            ans_ind.append(A.index(e))
    if len(ans_ind) <= 2:
        return "No"
    else:
        for b in BINGO:
            counter = 0
            for c in b:
                if c in ans_ind:
                    counter += 1
                if counter == 3:
                    return "Yes"
    return "No"
                    
                

def main():
    A = []
    for i in range(3):
        A += list(map(int, input().split()))
    N = int(input())
    B = []
    for i in range(N):
        B.append(int(input()))
    print(Main(A, N, B))

if __name__ == '__main__':
    main()