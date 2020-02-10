
def Main(N, K):
    ans = 0
    D = len(N)
    if K == 1:
        ans = 9*(D-1) + int(N[0])
    elif K == 2:
        if(D >= 3):
            ans = 9*9*(D-1) + 9*(D-2) + int(N[0]) + int(N[1])
        else:
            ans = 9*(D-1) + int(N[0])
    else:
        if(D >= 4):
            ans = 9*9*9*(D-1) + 9*9*(D-2) + 9*(D-1) +int(N[0]) + int(N[1]) + int(N[2])   
        elif(D == 3):
            ans = 9*9*(D-1) + 9*(D-2) + int(N[0]) + int(N[1])
        else:
            ans = 9*(D-1) + int(N[0])
    return ans
            
        
        

def main():
    N = str(input())
    K = int(input())
    print(Main(N, K))

if __name__ == '__main__':
    main()