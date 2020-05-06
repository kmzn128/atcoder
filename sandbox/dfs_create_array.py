def dfs(ans, ind, arr, start, end):
    if ind == end:
        ans.append(arr.copy())
        return
    for i in range(start, end+1):
        arr[ind] = i
        dfs(ans, ind+1, arr, start, end)
        

def Main(X):
    ans = []
    ind = 0
    start = 1
    end = X
    arr = [start]*end
    dfs(ans, ind, arr, start, end)
    return ans
    

def main():
    print(Main(3))

if __name__ == '__main__':
    main()