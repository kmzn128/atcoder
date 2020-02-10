import sys
input = sys.stdin.readline

def Main(s, t):
    ls = len(s)
    lt = len(t)
    dp = [[[] for _ in range(ls+1)] for _ in range(lt+1)]
    for i in range(lt):
        for j in range(ls):
            if(t[i] == s[j]):
                dp[i+1][j+1] = dp[i][j] + [t[i]]
            else:
                if(len(dp[i+1][j]) > len(dp[i][j+1])):
                    dp[i+1][j+1] = dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
                
    return "".join(dp[lt][ls])

def main():
    s = input().rstrip('\n')
    t = input().rstrip('\n')
    print(Main(s, t))

if __name__ == '__main__':
    main()