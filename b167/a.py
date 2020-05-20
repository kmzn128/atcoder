def Main(S,T):
    return 'Yes' if T[:-1] == S else 'No'

def main():
    S = str(input())
    T = str(input())
    print(Main(S,T))

if __name__ == '__main__':
    main()