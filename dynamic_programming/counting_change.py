import math
def counting_change(amount, coins, i=0, memo={}):
  key = (amount, i)
  if key in memo:
    return memo[key]
  
  if amount == 0:
    return 1
  if amount < 0:
    return 0
  if i == len(coins):
    return 0
  
  res = 0
  coin = coins[i]
  for quantity in range(0, (amount // coin) + 1):
    # print("amount", amount-coin*i, "coin", coin, "i", i)
    res += counting_change(amount-coin*quantity, coins, i+1, memo)
  
  memo[key] = res
  return res

# counting change
# Write a function, counting_change, that takes in an amount and a list of coins. The function should return the number of different ways it is possible to make change for the given amount using the coins.

# You may reuse a coin as many times as necessary.

# For example,

# counting_change(4, [1,2,3]) -> 4

# There are four different ways to make an amount of 4:

# 1. 1 + 1 + 1 + 1
# 2. 1 + 1 + 2
# 3. 1 + 3
# 4. 2 + 2
# test_00:
counting_change(4, [1, 2, 3]) # -> 4
# test_01:
counting_change(8, [1, 2, 3]) # -> 10

# solution
# dynamic programming with memoization
# def counting_change(amount, coins):
#   return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, i, memo):
  key = (amount, i)
  if key in memo:
    return memo[key]
  
  if amount == 0:
    return 1
  
  if i == len(coins):
    return 0
  
  coin = coins[i]
  
  total_count = 0
  for qty in range(0, (amount // coin) + 1):
    remainder = amount - (qty * coin)
    total_count += _counting_change(remainder, coins, i + 1, memo)
    
  memo[key] = total_count
  return total_count

# a = amount
# c = # coins
# Time: O(a*c)
# Space: O(a*c)