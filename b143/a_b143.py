A, B = map(int, input().split())
rest = A - 2 * B
if(rest > 0):
    print(rest)
else:
    print(0)