def Main(N):
    ans = 0
    for i in range(1,N+1):
        if i%15 == 0 or i%5 == 0 or i%3 == 0:
            continue
        else:
            ans += i
    return ans
    

def main():
    N = int(input())
    print(Main(N))

if __name__ == '__main__':
    main()