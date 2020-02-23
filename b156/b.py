def Main(N, K):
    counter = 0
    while(N):
        N //= K
        counter += 1
    return counter
    

def main():
    N, K = list(map(int, input().split()))
    print(Main(N, K))

if __name__ == '__main__':
    main()