W, A, B = map(int, input().split())
def Main(W, A, B):
    if A+W < B:
        return B-A-W
    elif B+W < A:
        return A-B-W
    else:
        return 0
    
print(Main(W, A, B))
