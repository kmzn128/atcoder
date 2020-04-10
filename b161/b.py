import math
import bisect
def Main(N, M, A):
    A.sort()
    wa = sum(A)
    thres = math.ceil(wa/(4*M))
    i = bisect.bisect_left(A, thres)
    return "Yes" if len(A)-i >= M else "No"
    

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(Main(N, M, A))

if __name__ == '__main__':
    main()