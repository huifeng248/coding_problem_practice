def pair_sum(numbers, target_sum):
  new_set = {}
  for index, num in enumerate(numbers):
    diff = target_sum - num
    if num not in new_set: 
      new_set[diff] = index
    else:
      # num_idx = numbers.index(num)
      # diff_idx = numbers.index(target_sum-num)
      return (new_set[num], index)

    
print(pair_sum([3, 2, 5, 4, 1], 8))


# pair sum
# Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.

# test_00:
# pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)
# test_01:
# pair_sum([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)
# test_02:
# pair_sum([4, 7, 9, 2, 5, 1], 3) # -> (3, 5)
# test_03:
# pair_sum([1, 6, 7, 2], 13) # -> (1, 2)
# test_04:
# pair_sum([9, 9], 18) # -> (0, 1)
# test_05:
# pair_sum([6, 4, 2, 8 ], 12) # -> (1, 3)

# using a hashmap (dictionary)
def pair_sum(numbers, target_sum):
  previous_numbers = {}
  
  for index, num in enumerate(numbers):
    complement = target_sum - num
    
    if complement in previous_numbers:
      return (index, previous_numbers[complement])
    
    previous_numbers[num] = index
# n = length of numbers list
# Time: O(n)
# Space: O(n)