DIRECT ( Problem -> Algorithm )
Example: gcd(a, b):  d from a - 1 to 1 and check if d divides both a and b
Example: fibonacci with direct recursive solution

INDIRECT ( Problem -> Thinking -> New Algorithm )
Example: gcd(a, b): gcd(a, b) == gcd(b, a mod b) with gcd(n, 0) = n
Example: fibonacci with matrices operations 
-----------------------------------------------------------------------

DIRECT apprach: find the maximum continous sum
find all the negative indices
if len(negative_indices) == 0:
  return sum(arr)
if len(negative_indices) >= len(arr) - 1
  return max(arr)
split the arr wherever negative elements and return max of (splits)
 
INDIRECT approach: (all cases taken care of IN A FEW LINES)
max_sum = curr_sum = a[0]
for num a[1:]:
  # -1 -2 1 2 3 -1 -11 -0.5 0
  # first we store the max negative number; 
  # once +ves start like 1 2 3 -ve -ve 2 as soom as you hit (POSITIVE or small -ve) the curr_sum RESTARTS
  curr_sum = max(curr_sum + n, n)
  # max_sum remembers the max sum we have seen yet coz curr_sum is oblivious to it 
  max_sum = max(curr_sum, max_sum)
