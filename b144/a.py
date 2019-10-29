import sys
input = sys.stdin.readline

def Main(a, b):
    if(a > 0 and a < 10 and b > 0 and b < 10):
        return a*b
    else: 
        return -1

def main():
    A, B = map(int, input().split())
    print(Main(A, B))

if __name__ == '__main__':
    main()