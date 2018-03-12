def isort(arr):
    for i in range(len(arr)):
        element = arr[i]
        j = i
        while j > 0 and arr[j - 1] > element: #while the prev element is greater than current element copy it forward
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = element
        
        
isort([9, 8, 1, 4, 5, 3, -1])
