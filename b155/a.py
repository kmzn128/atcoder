def Main(A, B, C):
    if A == B and A != C:
        return 'Yes'
    elif B == C and A != B:
        return 'Yes'
    elif A == C and A != B:
        return 'Yes'
    else:
        return 'No'

def main():
    A, B, C = list(map(int, input().split()))
    print(Main(A, B, C))

if __name__ == '__main__':
    main()