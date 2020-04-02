def Main(X, Y, A, B, C, p, q, r):
    p.sort()
    q.sort()
    r.sort()
    ans = 0
    p = p[-X:]
    q = q[-Y:]
    wa = X+Y
    for i in range(wa):
        if(len(r) and len(p) and len(q)):
            if p[-1] < r[-1] and q[-1] < r[-1]:
                ans += r.pop()
            elif p[-1] < q[-1]:
                ans += q.pop()
            else:
                ans += p.pop()
        elif(len(r) == 0 and len(p) and len(q)):
            if p[-1] < q[-1]:
                ans += q.pop()
            else:
                ans += p.pop()
        elif(len(r) and len(p)==0 and len(q)):
            if q[-1] < r[-1]:
                ans += r.pop()
            else:
                ans += q.pop()
        elif(len(r) and len(p) and len(q)==0):
            if p[-1] < r[-1]:
                ans += r.pop()
            else:
                ans += p.pop()
        elif(len(r)==0 and len(p)==0 and len(q)):
            ans += q.pop()
        elif(len(r)==0 and len(p) and len(q)==0):
            ans += p.pop()
        elif(len(r) and len(p)==0 and len(q)==0):
            ans += r.pop()
    return ans
def main():
    X, Y, A, B, C = map(int, input().split())
    p = list(map(int, input().split())) 
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    print(Main(X, Y, A, B, C, p, q, r))

if __name__ == '__main__':
    main()