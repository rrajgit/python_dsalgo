def pair_sum(arr, target):
    res = []
    seen = set()
    
    for num in arr:
        val = target - num
        if val in seen:
            res.append((min(num, val), max(num, val)))
        
        seen.add(num)
    
    return res
    
pair_sum([1, 2, 3, 2], 4)
