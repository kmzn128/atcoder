import sys
input = sys.stdin.readline
import bisect
import numpy as np

def Main(N, K, A, F):
    A.sort()
    F.sort()
    for i in range(K):
        mx = A.pop()-1
        bisect.insort_right(A, mx)
        if(mx < 0):
            break
    A.sort(reverse=True)
    a = np.array(A)
    f = np.array(F)
    return max(a*f)

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    F = list(map(int, input().split()))
    print(Main(N, K, A, F))

if __name__ == '__main__':
    main()