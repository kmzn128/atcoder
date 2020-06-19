N, A, B = map(int, input().split())
V = list(map(int, input().split()))

from collections import Counter
from itertools import combinations

def factorial(start, N):
    ans = 1
    for i in range(start, N+1):
        ans *= i
    return ans

def choose(n, m):
    a = factorial(n-m+1, n)
    b = factorial(1, m)
    return a/b

def Main(N, A, B, V):
    V.sort()
    V.reverse()
    counter_V = Counter(V)
    V_A = V[A-1]
    count_VA = counter_V[V_A]
    V_begin = 0
    V_end = N-1
    flag = True
    for i in range(N):
        if V[i] == V_A and flag:
            V_begin = i
            flag = False
        elif V[i] < V_A:
            V_end = i-1
            break
    V_edge = V_end
    if V[V_end] == V[B-1]:
        V_edge = B-1
    choose_num = 0
    for i in range(A-1, V_edge+1):
        choose_num += choose(V_end-V_begin+1, i-V_begin)
    return sum(V[:A])/A, choose_num
                     
ave, choose_num = Main(N, A, B, V)
print(ave)
print(choose_num)