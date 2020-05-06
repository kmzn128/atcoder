def Main(S, W):
    return 'unsafe' if S <= W else 'safe'

def main():
    S, W = map(int, input().split())
    print(Main(S, W))

if __name__ == '__main__':
    main()