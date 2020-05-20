A, Op, B = map(str, input().split())

def Main(A, Op, B):
    a = int(A)
    b = int(B)
    if Op == "+":
        return a+b
    if Op == '-':
        return a-b

print(Main(A, Op, B))