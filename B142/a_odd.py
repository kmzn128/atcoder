N = int(input())
def odd(N):
    if(N == 1):
        return 1.0
    if(N % 2 == 0):
        return 0.5
    else:
        return ((N-1)/2+1)/N

  
print(odd(N))      