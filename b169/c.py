import math

a, b = map(str, input().split())
A = int(a)
bb = b.replace(".","")
B = int(bb)

def Main(A, B):
    return A*B//100
                    
out = Main(A, B)
print(out)