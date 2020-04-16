from math import floor
def Main(A, B):
    for i in range(1, 1001):
        if floor(i*0.08) == A and floor(i*0.1) == B:
            return i
    return -1
    
def main():
    A, B = map(int, input().split())
    print(Main(A, B))

if __name__ == '__main__':
    main()