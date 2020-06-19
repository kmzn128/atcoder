X, Y = map(int, input().split())
from math import floor
def Main(X, Y):
    a = (Y-2*X)/2
    b = (4*X-Y)/2
    
    if a < 0 or b < 0:
        return "No"
    elif (a > 0 and floor(a) == a) or (b > 0 and floor(b) == b):
        return "Yes"
    else:
        return "No"
        
    
res = Main(X, Y)
print(res)