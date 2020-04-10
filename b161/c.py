def Main(N, K):
    if K == 1:
        return 0
    mo = N%K
    if K//2 <= mo:
        return K-mo
    else:
        return mo
         
    

def main():
    N, K = map(int, input().split())
    print(Main(N, K))

if __name__ == '__main__':
    main()