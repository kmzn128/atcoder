def Main(N, M):
    return N*(N-1)//2+M*(M-1)//2

def main():
    N, M = map(int, input().split())
    print(Main(N, M))

if __name__ == '__main__':
    main()