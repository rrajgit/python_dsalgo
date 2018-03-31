def anagram(a, b):
    a = a.lower().replace(' ', '')
    b = b.lower().replace(' ', '')
    a_ht = create_ht(a)
    b_ht = create_ht(b)
    
    if a_ht == b_ht:
        return True
    return False
    
def create_table(word):
    ht = {}
    for letter in word:
        if letter in ht:
            ht[letter] += 1
        else:
            ht[letter] = 1
    return ht
            
anagram('I am Lord Voldemort', 'Tom Marvolo Riddle') 
