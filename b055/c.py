N, M = map(int, input().split())

def Main(N, M):
    if N+3 >= M:
        return M//2
    else:
        c_remain = M-N*2
        return N+c_remain//4
    
print(Main(N, M))
