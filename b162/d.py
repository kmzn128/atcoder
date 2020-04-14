def binary_search(target, left, right, nums):
    if(left > right):
        return -1
    mid = (right-left)//2 + left
    if(nums[mid] == target):
        return mid
    elif(nums[mid] < target):
        return binary_search(target, mid+1, right, nums)
    else:
        return binary_search(target, left, mid-1, nums)
def Main(N, S):
    ans = 0
    d = {'R':[], 'G':[], 'B':[]}
    for i, c in enumerate(S):
        d[c].append(i)
    
    lenb = len(d['B'])
    for i in d['R']:
        for j in d['G']:
            sub = 0
            lenb = len(d['B'])
            di = abs(i-j)
            mi = min(i,j)
            ma = max(i,j)
            a = mi-di
            b = ma+di
            x = binary_search(a, 0, lenb-1, d['B'])
            y = binary_search(b, 0, lenb-1, d['B'])
            if x>=0 and y>=0:
                sub = 2
            elif x>=0 or y>=0: 
                sub = 1
            ci = (i+j)//2
            cf = (i+j)/2
            if ci == cf:
                z = binary_search(ci, 0, lenb-1, d['B'])
                if z>=0:
                    sub += 1
            ans += lenb - sub
    return ans
        
    

def main():
    N = int(input())
    S = str(input())
    print(Main(N,S))

if __name__ == '__main__':
    main()