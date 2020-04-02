def Main(X):
    a, b = divmod(X, 500)
    c, d = divmod(b, 5)
    return a * 1000 + c * 5

def main():
    X = int(input())
    print(Main(X))

if __name__ == '__main__':
    main()