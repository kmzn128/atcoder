def Main(L):
    return (L/3)**3

def main():
    L = int(input())
    print('{:.12f}'.format(Main(L)))

if __name__ == '__main__':
    main()