
def Main(S, T, A, B, U):
    if(U == S):
        return str(A-1) + " " + str(B)
    else:
        return str(A) + " " + str(B-1)

def main():
    S, T = list(map(str, input().split()))
    A, B = list(map(int, input().split()))
    U = str(input())
    print(Main(S, T, A, B, U))

if __name__ == '__main__':
    main()