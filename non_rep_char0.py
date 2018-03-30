def non_rep(s):
    present = {}
    for c in s:
        present[c] = True
    res = ""
    for c in s:
        if present[c]:
            present[c] = False
            res += c
    return res
            
    
non_rep('travelling salesman')
non_rep('tree traversal')
