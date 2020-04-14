def check(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

def Main(S):
    N = len(S)
    a = S[:(N-1)//2]
    b = S[(N+2)//2:]
    return "Yes" if check(S) and check(a) and check(b) else "No"

def main():
    S = str(input())
    print(Main(S))

if __name__ == '__main__':
    main()