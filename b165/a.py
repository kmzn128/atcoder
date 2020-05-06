def Main(K, A, B):
    for i in range(A, B+1):
        if i%K == 0:
            return 'OK'
    return 'NG'

def main():
    K = int(input())
    A, B = map(int, input().split())
    print(Main(K, A, B))

if __name__ == '__main__':
    main()