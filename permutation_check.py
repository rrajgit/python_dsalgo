def create_table(a):
    a_table = {}
    for c in a:
        if c in a_table:
            a_table[c] += 1
        else:
            a_table[c] = 1

    return a_table

def is_permutation(a, b):

    a_table = create_table(a)
    b_table = create_table(b)

    for key in a_table:
        if key not in b_table:
            return False
        elif a_table[key] != b_table[key]:
            return False

    for key in b_table:
        if key not in a_table:
            return False
        elif b_table[key] != a_table[key]:
            return False
    return True


a = input().strip()
b = input().strip()
print(is_permutation(a, b))
