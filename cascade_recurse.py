def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

def inverse_cascade(n, hide):
    if hide <= 0:
        print(n)
    else:
        print(n // (10 ** hide))
        inverse_cascade(n, hide - 1)
        print(n // (10 ** hide))
        
cascade(12345)
print()
inverse_cascade(12345, 4)
