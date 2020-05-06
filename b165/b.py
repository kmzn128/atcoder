from math import floor
def Main(X):
    i = 1
    a = 100
    while True:
        a = floor(a*1.01)
        if a >= X:
            return i
        i += 1
        
def main():
    X = int(input())
    print(Main(X))

if __name__ == '__main__':
    main()