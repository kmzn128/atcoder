import sys
input = sys.stdin.readline
import math

def Main(a, b, x):
    h = x / (a*a)
    r = 0
    if(h >= b/2):
        r = math.atan2(b-h, a/2)
    else:
        y = 2*x/(a*b)
        r = math.atan2(b,y)
    return math.degrees(r)

def main():
    A, B, X = map(int, input().split())
    print(Main(A, B, X))


if __name__ == '__main__':
    main()