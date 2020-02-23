def Main(N, A):
    for z in A:
        if (z % 2 == 0):
            if (z % 3 == 0) or (z % 5 == 0):
                continue
            else:
                return 'DENIED'
    return 'APPROVED'  

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(Main(N, A))

if __name__ == '__main__':
    main()