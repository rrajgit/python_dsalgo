def quicksort(A, left, right):
    if left >= right:
        return
    m = partition(A, left, right)
    quicksort(A, left, m - 1)
    quicksort(A, m + 1, right)
    
def partition(A, left ,right):
    # pick the leftmost element as the pivot
    pivot = A[left]
    
    # j is the starting of the second half or part
    j = left
    for i in range(left, right  +1):
        # element <= pivot then we if j has started then swap
        if A[i] <= pivot:
            if j != left:
                A[i], A[j] = A[j], A[i]
                j = j + 1
        # otherwise if j is still the leftmost thing
        else:
            if j == left:
                j = i
    # 3 1 2 vs 1 2 3
    if j == left:
        j = right + 1
    A[left], A[j - 1] = A[j - 1], A[left]
    
    return j-1
    
#quicksort([6, 1, 2, 9, 11, 8, 3, 12], 0, 6)
quicksort([1,2, 3, 4, 5, 6, 7, 8], 0, 7)
