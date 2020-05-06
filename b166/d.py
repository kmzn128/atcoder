def Main(X):
    for i in range(-178, 178):
        for j in range(-178, 178):
            if i**5-j**5 == X:
                return i,j

def main():
    X = int(input())
    i, j = Main(X)
    print("{0} {1}".format(i, j))

if __name__ == '__main__':
    main()