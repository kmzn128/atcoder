A, B, C, D, E = map(int, input().split())

def Main(A, B, C, D, E):
    li = (A, B, C, D, E)
    for i in range(5):
        if li[i] == 0:
            return i+1

print(Main(A, B, C, D, E))
