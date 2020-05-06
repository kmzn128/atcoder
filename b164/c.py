def Main(N, S):
    d = {}
    for s in S:
        if s not in d:
            d[s] = 0
        else:
            d[s] += 1
    return len(d)
    
def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(str(input()))
    print(Main(N, S))

if __name__ == '__main__':
    main()