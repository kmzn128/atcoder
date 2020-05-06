def Main(N, M, A):
    return max(N - sum(A), -1)    

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(Main(N, M, A))

if __name__ == '__main__':
    main()