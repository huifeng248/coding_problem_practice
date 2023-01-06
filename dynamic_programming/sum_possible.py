def sum_possible(amount, numbers, memo={}):
  if amount in memo:
    return memo[amount]
#   base case
  if amount == 0:
    return True
  if amount < 0:
    return False
  
  for num in numbers:
#   A  need to record the memo at the final return 
    if sum_possible(amount-num, numbers, memo):
      memo[amount] = True
      return True
#   B  need to record the memo at the final return 
  memo[amount] = False
  return False 



# favorite
# sum possible
# Write a function sum_possible that takes in an amount and a list of positive numbers. The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary.

# You may assume that the target amount is non-negative.

# test_00:
sum_possible(8, [5, 12, 4]) # -> True, 4 + 4
# test_01:
sum_possible(15, [6, 2, 10, 19]) # -> False
# test_02:
sum_possible(13, [6, 2, 1]) # -> True
# test_03:
sum_possible(103, [6, 20, 1]) # -> True
# test_04:
sum_possible(12, []) # -> False
# test_05:
sum_possible(12, [12]) # -> True
# test_06:
sum_possible(0, []) # -> True
# test_07:
sum_possible(271, [10, 8, 265, 24]) # -> False
# test_08:
sum_possible(2017, [4, 2, 10]) # -> False
# test_09:
sum_possible(13, [3, 5]) # -> true


# solution
# dynamic programming with memoization
# def sum_possible(amount, numbers):
#   return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
  if amount in memo:
    return memo[amount]
  
  if amount < 0:
    return False
  
  if amount == 0:
    return True
  
  for num in numbers:
    if _sum_possible(amount - num, numbers, memo):
      memo[amount] = True
      return True
    
  memo[amount] = False  
  return False
# a = amount
# n = length of numbers
# Time: O(a*n)
# Space: O(a)