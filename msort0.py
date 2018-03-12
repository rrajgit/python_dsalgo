def merge_sort(arr, left, right):
    if right <= left:
        return
    else:
        merge_sort(arr, left, (left + right) // 2)
        merge_sort(arr, (left + right) // 2 + 1, right)
        merge(arr, left, (left + right) // 2,  (left + right) // 2 + 1, right)
        
def merge(arr, left1, right1, left2, right2):
    temp = [0] * (right2 - left1 + 1)
    ptr = 0
    ptr1 = left1
    ptr2 = left2
    while (ptr < right2 - left1 + 1):
        if ptr1 > right1:
            for i in range(ptr2, right2  +1):
                temp[ptr] = arr[i]
                ptr += 1
                
        elif ptr2 > right2:
            for i in range(ptr1, right1  +1):
                temp[ptr] = arr[i]
                ptr += 1
                
        else:
            if arr[ptr1] < arr[ptr2]:
                temp[ptr] = arr[ptr1]
                ptr1 += 1
            else:
                temp[ptr] = arr[ptr2]
                ptr2 += 1
            ptr += 1 
            
    for i in range(len(temp)):
        arr[left1 + i] = temp[i]
        
merge_sort([ 10, 9, -2, -3, 1, -4, -2], 0, 6)
