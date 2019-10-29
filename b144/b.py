import sys
input = sys.stdin.readline

def Main(n):
    ans = False
    for i in range(1, 10):
        if(n % i == 0):
            nn = n // i
            if(nn >= 10):
                ans = False
                continue
            if(n % nn == 0):
                ans = True
                break
    return 'Yes' if ans else 'No'
        

def main():
    N = int(input())
    print(Main(N))

if __name__ == '__main__':
    main()