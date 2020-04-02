def Main(S):
    return "Yes" if S[2] == S[3] and S[4] == S[5] else "No"

def main():
    S = str(input())
    print(Main(S))

if __name__ == '__main__':
    main()