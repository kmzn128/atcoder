import bisect
def Main(N, K, A):
    L_fu = []
    L_sei = []
#     A.sort()
    fu = list(filter(lambda x: x < 0, A))
    zero = list(filter(lambda x: x == 0, A))
    sei = list(filter(lambda x: x > 0, A))
    n_f = len(fu)
    n_z = len(zero)
    n_s = len(sei)
    fu.sort()
    sei.sort()
    m_f = n_f*n_s
    m_s = n_f*(n_f-1)//2+n_s*(n_s-1)//2
    if K <= m_f:
        for i in range(n_f):
            for j in range(n_s):
                bisect.insort_left(L_fu, fu[i]*sei[j])
        return L_fu[K-1]
    elif N*(N-1)//2 - K <= m_s:
        for i in range(n_f-1):
            for j in range(i+1, n_f):
                bisect.insort_left(L_sei, fu[i]*fu[j])
        for i in range(n_s-1):
            for j in range(i+1, n_s):
                bisect.insort_left(L_sei, sei[i]*sei[j])
        return L_sei[K-N*(N-1)//2-1]        
    else:
        return 0
    


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    print(Main(N, K, A))
    
if __name__ == '__main__':
    main()