s = "aabbaabb"
z = [len(s)]
def zalgo(s,z):
    for i in range(1, len(s)):
        zval = 0
        for j in range(0, len(s)-i):
            if(s[j] == s[i+j]):
                zval += 1
                continue
            else:
                z.append(zval)
                break

        
print(zalgo(s,z))