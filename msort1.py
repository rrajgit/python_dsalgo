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
    for i in range(len(temp)):
        # ptr2 >= right_size ptr1 < right1_size
        if ptr2 > right2 or (ptr1 <= right1 and arr[ptr1] < arr[ptr2]) :
            temp[i] = arr[ptr1]
            ptr1 += 1
        else:
            temp[i] = arr[ptr2]
            ptr2 += 1

            
    for i in range(len(temp)):
        arr[left1 + i] = temp[i]
        
merge_sort([ 10, 9, -2, -3, 1, -4, -2], 0, 6)
