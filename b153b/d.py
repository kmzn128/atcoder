import math
def Main(H):
    n = math.floor(math.log(H, 2))
    return 2**(n+1)-1

def main():
    H = int(input())
    print(Main(H))

if __name__ == '__main__':
    main()