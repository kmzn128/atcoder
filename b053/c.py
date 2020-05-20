x = int(input())
def Main(x):
    d, m = divmod(x, 11)
    if m == 0:
        return d*2
    else:
        return d*2+(m-1)//6+1
    
print(Main(x))
