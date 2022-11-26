# intersection
# Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.

# test_00:
# intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
# test_01:
# intersection([2,4,6], [4,2]) # -> [2,4]
# test_02:
# intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]
# test_03:
# intersection([0,1,2], [10,11]) # -> []
# test_04:
# a = [ i for i in range(0, 50000) ]
# b = [ i for i in range(0, 50000) ]
# intersection(a, b) # -> [0,1,2,3,..., 49999]



# def intersection(a, b):
#   duplicate = set()
#   for num in a:
#     if num in b and num not in duplicate:
#       duplicate.add(num)
  
#   return list(duplicate)

def intersection(a, b):
  union = a + b
  object = {}
  arr = []
  
  for num in union:
    if num not in object:
      object[num] = 1
    else:
      object[num] += 1
  
  for key in object:
    if object[key] == 2:
      arr.append(key)
  return arr


def intersection(a, b):
  arr = []
  
  a_set = set(a)
  for i in b:
    if i in a_set:
      arr.append(i)
  
  return arr


# solutions brute force (timeout)
def intersection(a, b):
  result = []
  for item in b:
    if item in a:
      result.append(item)
  return result
# n = length of array a, m = length of array b
# Time: O(n*m)
# Space: O(min(n,m))
# using set (pass)
def intersection(a, b):
  set_a = set(a)
  return [ item for item in b if item in set_a ]
# UI