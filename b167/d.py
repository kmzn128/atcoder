def Main(N, K, A):
    l = []
    for i in range(N):
        l.append([0,0])
    ind = A[0]-1
    l[ind][0] = 0
    l[ind][1] = 1
    detected = 0
    first = 0
    second = 0
    path = [0]
    path.append(ind)
    for i in range(1, N):
        ind = A[ind]-1
        if l[ind][1] == 1:
            detected = ind
            first = l[detected][0]
            second = i
            break
        else:
            l[ind][0] = i
            l[ind][1] = 1
            path.append(ind)
    if K < first:
        return path[K]+1
    else:
        return path[first + (K-first)%(second-first)]+1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(Main(N, K, A))

if __name__ == '__main__':
    main()