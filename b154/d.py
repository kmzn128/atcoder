
def Main(N, K, P):
    wa = sum(P[:K])
    max_sum = wa
    max_sum_ind = 0
    for i in range(N-K):
        wa = wa - P[i] + P[i+K]
        if(wa > max_sum):
            max_sum = wa
            max_sum_ind = i
    ans = 0
    if max_sum_ind == 0:
        for i in range(K):
            ans += (P[i]+1)/2
    else:
        for i in range(max_sum_ind+1, max_sum_ind+K+1):
            ans += (P[i]+1)/2
    return ans

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    print("{:.12f}".format(Main(N, K, P)))

if __name__ == '__main__':
    main()