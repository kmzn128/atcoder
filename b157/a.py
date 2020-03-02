def Main(N):
    return N//2+1 if N%2 else N//2

def main():
    N = int(input())
    print(Main(N))

if __name__ == '__main__':
    main()