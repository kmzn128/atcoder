N = str(input())

def Main(N):
    c = N[-1]
    n = int(c)
    if n in [2,4,5,7,9]:
        return 'hon'
    elif n in [0,1,6,8]:
        return 'pon'
    else:
        return 'bon' 

print(Main(N))
