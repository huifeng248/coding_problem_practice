# linked list values
# Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

# Hey. This is our first linked list problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# linked_list_values(a) # -> [ 'a', 'b', 'c', 'd' ]
# test_01:
# x = Node("x")
# y = Node("y")

# x.next = y

# # x -> y

# linked_list_values(x) # -> [ 'x', 'y' ]
# test_02:
# q = Node("q")

# # q

# linked_list_values(q) # -> [ 'q' ]
# test_03:
# linked_list_values(None) # -> [ ]

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def linked_list_values(head):
#   arr = []
#   current = head
#   while current is not None:
#     arr.append(current.val)
#     current = current.next
#   return arr

def linked_list_values(head):
  arr = []
  if head is None:
    return arr
  print("before", arr)
  arr.append(head.val)
  print("after", arr)
  
  return arr + linked_list_values(head.next)




def linked_list_values(head):
  values = []
  
  fill_values(head, values)
  return values

def fill_values(head, values):
  if head is None:
    return 
  
  values.append(head.val)
  return fill_values(head.next, values)

# solutions
# iterative
def linked_list_values(head):
  values = []
  current = head
  while current is not None:
    values.append(current.val)
    current = current.next
  return values
# n = number of nodes
# Time: O(n)
# Space: O(n)
# recursive
def linked_list_values(head):
  values = []
  _linked_list_values(head, values)
  return values

def _linked_list_values(head, values):
  if head is None:
    return
  values.append(head.val)
  _linked_list_values(head.next, values)
# n = number of nodes
# Time: O(n)
# Space: O(n)