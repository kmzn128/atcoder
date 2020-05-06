def Main(A,B,C,D):
    while True:
        C -= B
        if C <= 0:
            return "Yes"
        A -= D
        if A <= 0:
            return "No"
        
def main():
    A, B, C, D = map(int, input().split())
    print(Main(A, B, C, D))

if __name__ == '__main__':
    main()