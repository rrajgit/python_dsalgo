def compress(s):
    res = ""
    i = 0
    while i < len(s):
        ele = s[i]
        j = i + 1
        while j < len(s) and s[j] == ele:
            j += 1
            
        res = res + ele + str(j - i)
        i = j
    return res
        
print(compress('AAABB'))
print(compress('A'))
print(compress('AAABCCDDDDD'))
print(compress('AAaa'))
