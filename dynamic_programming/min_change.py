# this is also applicable for max change for the coin

def min_change(amount, coins):
  res = _min_change(amount, coins, memo={})
  if res == float('inf'):
    return -1
  else:
    return res

def _min_change(amount, coins, memo={}):
  if amount in memo:
    return memo[amount]
  
  if amount == 0:
    return 0
  
  if amount < 0:
    return float('inf')
  
  min_path = float('inf')
  
  for coin in coins:
    path = _min_change(amount-coin, coins) + 1
    min_path = min(min_path, path)
  
  memo[amount] = min_path
  return min_path

# min change
# Write a function min_change that takes in an amount and a list of coins. The function should return the minimum number of coins required to create the amount. You may use each coin as many times as necessary.

# If it is not possible to create the amount, then return -1.

# test_00:
min_change(8, [1, 5, 4, 12]) # -> 2, because 4+4 is the minimum coins possible
# test_01:
min_change(13, [1, 9, 5, 14, 30]) # -> 5
# test_02:
min_change(23, [2, 5, 7]) # -> 4
# test_03:
min_change(102, [1, 5, 10, 25]) # -> 6
# test_04:
min_change(200, [1, 5, 10, 25]) # -> 8
# test_05:
min_change(2017, [4, 2, 10]) # -> -1
# test_06:
min_change(271, [10, 8, 265, 24]) # -> -1
# test_07:
min_change(0, [4, 2, 10]) # -> 0
# test_08:
min_change(0, []) # -> 0