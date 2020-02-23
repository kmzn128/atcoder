
def main():
    N = int(input())
    S = {}
    for i in range(N):
        K = str(input())
        if(K not in S):
            S[K] = 0
        else:
            S[K] += 1
    max_v = max(S.items(), key = lambda x: x[1])
    print(max_v)
    ans = []
    for k, v in S.items():
        if v == max_v[1]:
            ans.append(k)
    ans.sort()
    for a in ans:
        print(a)
#     print(k[v.index(max(v))])
#     print(max(S, key=lambda k: S[k]))
#     print(Main(N, S))

if __name__ == '__main__':
    main()