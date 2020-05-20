def Main(A, B, C, K):
    if K < A:
        return K
    elif A <= K <= A+B:
        return A
    else:
        return 2*A+B-K
        
def main():
    A, B, C, K = map(int, input().split())
    print(Main(A, B, C, K))

if __name__ == '__main__':
    main()