
def Main(N, A):
    A.sort()
    for i in range(N):
        if(A[i] == A[i-1]):
            return "NO"
    return "YES"

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(Main(N, A))

if __name__ == '__main__':
    main()