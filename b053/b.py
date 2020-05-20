S = str(input())

def Main(S):
    ans = 0
    candidate = 0
    flag = False
    for c in S:
        if c == 'A':
            flag = True
        if flag:
            candidate += 1
            if c == 'Z':
                ans = candidate
    return ans
            
    
res = Main(S)
print(res)