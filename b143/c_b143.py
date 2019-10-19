N = int(input())
S = input()
li = []
for c in S:
    if(len(li) == 0):
        li.append(c)
    else:
        pe = li[-1]
        if(pe == c):
            continue
        else:
            li.append(c)
print(len(li))
