def max_cont_sum(arr):
  curr_sum = max_sum = arr[0]
  
  for num in arr[1:]
    curr_sum = max(curr_sum + num, num)
    max_sum = max(curr_sum, max_sum)
    
  return max_sum
  
max_cont_sum([-1, -2, -3])
max_cont_sum([-2, -2, 2, -2, -2)]
max_cont_sum([-1, -2, 1, 2, 3, -9, 3, 4, 5, -10])
