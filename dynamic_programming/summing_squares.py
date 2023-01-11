import math
def summing_squares(n, memo={}):
  if n in memo:
    return memo[n]
  
  if n ==0:
    return 0
  if n == 1:
    return 1
  
  res = float('inf')
  for i in reversed(range(math.ceil(math.sqrt(n)), 0, -1)):
    if n - i**2 >=0:
      path = summing_squares(n - i**2, memo) + 1
    res = min(res, path)
  
  memo[n] = res
  return res
  
#   solution 2
import math
def summing_squares(n, memo={}):
  if n in memo:
    return memo[n]
  
  if n ==0:
    return 0
  # if n == 1:
  #   return 1
  
  res = float('inf')
  for i in range(1, math.ceil(math.sqrt(n))+1):
    if n - i**2 >=0:
      path = summing_squares(n - i**2, memo) + 1
    res = min(res, path)
  
  memo[n] = res
  return res

# solution
# dynamic programming with memoization
# import math

def summing_squares(n):
  return _summing_squares(n, {})

def _summing_squares(n, memo):
  if n in memo:
    return memo[n]
  
  if n == 0:
    return 0
  
  min_squares = float('inf')
  for i in range(1, math.floor(math.sqrt(n) + 1)):
    square = i * i
    num_squares = 1 + _summing_squares(n - square, memo)
    min_squares = min(min_squares, num_squares)
  
  memo[n] = min_squares
#   return min_squares
# n = length of nums
# Time: O(n * sqrt(n))
# Space: O(n)

# summing squares
# Write a function, summing_squares, that takes a target number as an argument. The function should return the minimum number of perfect squares that sum to the target. A perfect square is a number of the form (i*i) where i >= 1.

# For example: 1, 4, 9, 16 are perfect squares, but 8 is not perfect square.

# Given 12:

# summing_squares(12) -> 3

# The minimum squares required for 12 is three, by doing 4 + 4 + 4.

# Another way to make 12 is 9 + 1 + 1 + 1, but that requires four perfect squares.
# test_00:
summing_squares(8) # -> 2
# test_01:
summing_squares(9) # -> 1
# test_02:
summing_squares(12) # -> 3
# test_03:
summing_squares(1) # -> 1
# test_04:
summing_squares(31) # -> 4
# test_05:
summing_squares(50) # -> 2
# test_06:
summing_squares(68) # -> 2
# test_07:
summing_squares(87) # -> 4