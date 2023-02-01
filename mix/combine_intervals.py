from collections import deque

# def sort_fn(x):
#   return x[0]

def combine_intervals(intervals):
  #sort into a sorted intervals
  # combine the sorted
  # if len(intervals) <=1:
  #   return intervals
  # mid = len(intervals)//2
  # left = combine_intervals(intervals[:mid])
  # right = combine_intervals(intervals[mid:])
  # sorted_interval = sorted(left, right)
  # sorted_interval = sorted(intervals, key = sort_fn)
  sorted_interval = sorted(intervals, key = lambda x: x[0])
  
  
  res = combine(sorted_interval)
  return res

# def sorted(left, right):
#   res = []
#   left = deque(left)
#   right = deque(right)
#   while left and right:
#     if left[0][0] <= right[0][0]:
#       res.append(left[0])
#       left.popleft()
#     else:
#       res.append(right[0])
#       right.popleft()
#   if left:
#     res += list(left)
#   if right:
#     res+= list(right)
#   return res 

def combine(sorted_interval):
  # for index, interval in enumerate(sorted_intervals):
  res = [sorted_interval[0]]
  for current in sorted_interval[1:]:
    last_start, last_end = res[-1]
    if last_end>=current[0]:
      if last_end < current[1]:
        res[-1] = (last_start, current[1])
    else:
      res.append(current)

  return res 
      

    
    
  
# intervals = [
#   (6, 8),
#   (2, 9),
#   (10, 12),
#   (20, 24),
# ]
# # intervals = [(2, 9), (6, 8), (10, 12), (20, 24)] 
# print(combine_intervals(intervals))
# # print(combine(intervals))


# solution
# sort and combine
def combine_intervals(intervals):
  sorted_intervals = sorted(intervals, key=lambda x : x[0])
  combined = [ sorted_intervals[0] ]
  
  for current_interval in sorted_intervals[1:]:
    last_start, last_end = combined[-1]
    current_start, current_end = current_interval
    
    if current_start <= last_end:
      if current_end > last_end:
        combined[-1] = (last_start, current_end)
    else:
      combined.append(current_interval)
      
  return combined
  
# n = number of intervals
# Time: O(nlogn)
# Space: O(n)
    
  


