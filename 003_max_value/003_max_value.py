# Write a function, max_value, that takes in list of numbers as an argument. The function should return the largest number in the list.

# Solve this without using any built-in list methods.

# You can assume that the list is non-empty.


def max_value(nums):
  # pass # todo
  max = float('-inf')
  for num in nums:
    if num > max:
      max = num
    else:
      pass
  return max


# solution
def max_value(nums):
  maximum = float('-inf')
  
  for num in nums:
    if num > maximum:
      maximum = num
      
  return maximum


# n = length of list
# Time: O(n)
# Space: O(1)