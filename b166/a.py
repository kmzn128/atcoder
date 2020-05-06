def Main(S):
    d = {"ABC":"ARC", "ARC":"ABC"}
    return d[S]

def main():
    S = str(input())
    print(Main(S))

if __name__ == '__main__':
    main()