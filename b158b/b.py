def Main(N, A, B):
    di, mo = divmod(N, A+B)
    return di*A + min(mo, A)

def main():
    N, A, B = map(int, input().split())
    print(Main(N, A, B))

if __name__ == '__main__':
    main()