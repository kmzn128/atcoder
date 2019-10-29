import sys
input = sys.stdin.readline
import math

def Main(n):
    fl = math.floor(math.sqrt(n))
    a = b = 0
    for i in range(fl, 0, -1):
        if(n % i == 0):
            a = n // i
            break
    b = n // a
    return a + b - 2   

def main():
    N = int(input())
    print(Main(N))


if __name__ == '__main__':
    main()