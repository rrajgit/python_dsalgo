def unique_char(s):
  
  ascii_arr = [False] * 256
  
  for c in s:
    if ascii_arr[ord(c)]:
      return False
    ascii_arr[ord(c)] = True
  return True
