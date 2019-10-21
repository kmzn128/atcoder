s = input()
def f(s):
    even = False
    for c in s:
        if(even):
            if(c == 'R'):
                return 'No'
            even = False
        else:
            if(c == 'L'):
                return 'No'
            even = True
    return 'Yes'
print(f(s))