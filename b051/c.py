Sx, Sy, Tx, Ty = map(int, input().split())

def Main(Sx, Sy, Tx, Ty):
    x = Tx - Sx
    y = Ty - Sy
    dir = ['U','R','D','L','U','R','D','R','D','L','U']
    steps = [y, x, y, x+1, y+1, x+1, 1, 1, y+1, x+1, 1]
    ans = []
    for d, s in zip(dir, steps):
        ans.append(d*s)
    return "".join(ans)
          
                    
print(Main(Sx, Sy, Tx, Ty))