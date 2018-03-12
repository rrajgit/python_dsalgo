def quicksort(A, left, right):
    if left >= right:
        return
    m = partition(A, left, right)
    quicksort(A, left, m - 1)
    quicksort(A, m + 1, right)
    
def partition(A, left ,right):
    pivot = A[left]
    
    j = left
    for i in range(left, right  +1):
        if A[i] <= pivot:
            if j != left:
                A[i], A[j] = A[j], A[i]
                j = j + 1
        else:
            if j == left:
                j = i
    if j == left:
        j = right + 1
    A[left], A[j - 1] = A[j - 1], A[left]
    
    return j-1
    
#quicksort([6, 1, 2, 9, 11, 8, 3, 12], 0, 6)
quicksort([1,2, 3, 4, 5, 6, 7, 8], 0, 7)
