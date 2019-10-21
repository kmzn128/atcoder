N = int(input())
S = input()
count = N//2
def check(n, N, s):
    for i in range(n, 0, -1):
        for j in range(0, N-2*i+1):
            for k in range(j+i, N-i+1):
                if(s[j] == s[k]):
                    if(s[j:j+i] == s[k:k+i]):
                        return i
    return 0
print(check(count, N, S))                    
     