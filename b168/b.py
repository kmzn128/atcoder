K = int(input())
S = str(input())

def Main(K, S):
    if len(S) <= K:
        return S
    else:
        return S[:K] + '...'
        
res = Main(K, S)
print(res)