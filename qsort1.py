def quicksort(A, left, right):
    if left >= right:
        return
    m = partition(A, left, right)
    quicksort(A, left, m - 1)
    quicksort(A, m + 1, right)
    
def partition(A, left ,right):
    # pick the leftmost element as the pivot
    pivot = A[left]
    
    # j is the END OF THE FIRST PART
    j = left
    for i in range(left+1 , right  +1):
        # element <= pivot then we if 
        if A[i] <= pivot:
            j += 1
            A[i], A[j] = A[j], A[i]

    A[left], A[j] = A[j], A[left]
    
    return j
    
#quicksort([6, 1, 2, 9, 11, 8, 3, 12], 0, 6)
quicksort([1,2, 3, 4, 5, 6, 7, 8], 0, 7)
