def binary_search(numbers, target):
  low = 0
  high = len(numbers)-1
  while low <= high:
    mid = (low+high)//2
    print(mid, low, high, numbers[mid])
    if numbers[mid] == target:
      return mid
    if target > numbers[mid]:
      # print("111low", low, "high", high)
      low = mid +1
    if target < numbers[mid]:
      # print("2222low", low, "high", high)
      
      high = mid -1
      
  return -1

print(binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 27)) 


# binary search
def binary_search(numbers, target):
  lo = 0
  hi = len(numbers) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    if target < numbers[mid]:
      hi = mid - 1
    elif target > numbers[mid]:
      lo = mid + 1
    else:
      return mid
  return -1
# n = length of numbers array
# Time: O(logn)
# Space: O(1)


# Write a function, binary_search, that takes in a sorted list of numbers and a target. The function should return the index where the target can be found within the list. If the target is not found in the list, then return -1.

# You may assume that the input array contains unique numbers sorted in increasing order.

# Your function must implement the binary search algorithm.

# test_00
# binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8], 6) # -> 6
# test_01
# binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 27) # -> -1