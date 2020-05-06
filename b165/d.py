from math import floor
def Main(A, B, N):
    if N < B:
        return floor(A*N/B)-A*floor(N/B)
    else:
        return floor(A*(B-1)/B)-A*floor((B-1)/B)

def main():
    A, B, N =map(int, input().split()) 
    print(Main(A, B, N))

if __name__ == '__main__':
    main()