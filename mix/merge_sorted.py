from collections import deque
def merge_sort(nums):
  if len(nums) <= 1:
    return nums
  
  mid = len(nums)//2

  left = merge_sort(nums[:mid])
  right = merge_sort(nums[mid:])
  
  return merge(left, right)

def merge(left, right):
  left = deque(left)
  right = deque(right)
  res = []
  while left and right:
    if left[0] <= right[0]:
      res.append(left[0])
      left.popleft()
    else:
      res.append(right[0])
      right.popleft()
      
  if left:
    res += left
  if right:
    res += right

  return res
  
    