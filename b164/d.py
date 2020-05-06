def checker(s, n, int_s):
#    print(s)
    su = sum(int_s)
    if su%3 != 0:
        return False
    if n <= 10:
        i = int("".join(s))
        return i%673 == 0
    else:
        sub = int(s[-1])*2
        suba = int("".join(s[-4:-1]))
        subb = suba - sub
        new_s = s[:-4] + str(subb)
        new_int_s = int_s[:-4] + [int(c) for c in str(subb)]
        checker(new_s, n-1, new_int_s)
    

def Main(S):
    le = len(S)
    int_s = [int(c) for c in S]
    if(0 <= le <= 3):
        return 0
    ans = 0
    for i in range(le-3):
        for j in range(i+4, le+1):
            s = S[i:j]
            lee = len(s)
            if checker(s, lee, int_s[i:j]):
                ans += 1
    return ans
            


def main():
    S = str(input())
    print(Main(S))

if __name__ == '__main__':
    main()