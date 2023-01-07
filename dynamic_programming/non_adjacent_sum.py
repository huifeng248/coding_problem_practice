def non_adjacent_sum(nums, memo={}):
  arr = tuple(nums)
  if arr in memo:
    return memo[arr]
  
  if len(nums) == 0:
    return 0
  
  if len(nums) == 1:
    return nums[0]
  
  if len(nums) ==2:
    return max(nums[0], nums[1])
  
  take_first = nums[0] + non_adjacent_sum(nums[2:], memo)
  non_take_first = non_adjacent_sum(nums[1:], memo)
  
  memo[arr] = max(take_first, non_take_first)
  return max(take_first, non_take_first)
  
  

# nums = [2, 4, 5, 12, 7]
# print(non_adjacent_sum(nums)) # -> 16

# solution
# dynamic programming with memoization
def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, 0, {})

def _non_adjacent_sum(nums, i, memo):
  if i in memo:
    return memo[i]
  
  if i >= len(nums):
    return 0
  
  include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
  exclude = _non_adjacent_sum(nums, i + 1, memo)
  memo[i] = max(include, exclude)
  return memo[i]
# n = length of nums
# Time: O(n)
# Space: O(n)