
def Main(S):
    N = len(S)
    return "".join(['x' for _ in range(N)])

def main():
    S = str(input())
    print(Main(S))

if __name__ == '__main__':
    main()