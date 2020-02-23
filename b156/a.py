def Main(N, R):
    if N >= 10:
        return R
    else:
        return R + 100*(10-N)

def main():
    N, R = list(map(int, input().split()))
    print(Main(N, R))

if __name__ == '__main__':
    main()