A, B = map(int, input().split())
def Main(A, B):
    if A == B:
        return 'Draw'
    elif A == 1:
        return 'Alice'
    elif B == 1:
        return 'Bob'
    else:
        return 'Alice' if A > B else 'Bob'
    
print(Main(A, B))
