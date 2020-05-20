import math

A, B, H, M = map(int, input().split())

def Main(A, B, H, M):
    th1 = 2*math.pi/12
    th2 = 2*math.pi/60
    t1 = th1*H+(2*math.pi*M/(12*60))
    t2 = th2*M
    return math.sqrt((A*math.cos(t1)-B*math.cos(t2))**2 +
            (A*math.sin(t1)-B*math.sin(t2))**2)
          
                    
out = Main(A, B, H, M)
print('{:.20f}'.format(out))