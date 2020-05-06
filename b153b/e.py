def Main(H, N, A, B):
    
    
    dp = [0]*(H+10000)
    for i in range(1, H+10001):
        pass
        
    
        

def main():
    H, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(Main(H, N, A, B))

if __name__ == '__main__':
    main()