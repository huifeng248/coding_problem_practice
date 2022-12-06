# create linked list
# Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each item of the list as the values of the nodes. The function should return the head of the linked list.

# test_00:
create_linked_list(["h", "e", "y"])
# h -> e -> y
# test_01:
create_linked_list([1, 7, 1, 8])
# 1 -> 7 -> 1 -> 8
# test_02:
create_linked_list(["a"])
# a
# test_03:
create_linked_list([])
# null


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def create_linked_list(values):
#   dummy_head = Node(None)
#   tail = dummy_head
#   for ele in values: 
#     tail.next = Node(ele)
#     tail = tail.next
#   return dummy_head.next
    
def create_linked_list(values, i = 0):
  if i == len(values):
    return None
  head = Node(values[i])
  head.next = create_linked_list(values, i+1)
  return head


# solutions
def create_linked_list(values):
  dummy_head = Node(None)
  tail = dummy_head
  for val in values:
    tail.next = Node(val)
    tail = tail.next
  return dummy_head.next
# n = length of values
# Time: O(n)
# Space: O(n)
# recursive
def create_linked_list(values, i = 0):
  if i == len(values):
    return None
  head = Node(values[i])
  head.next = create_linked_list(values, i + 1)
  return head
# n = length of values
# Time: O(n)
# Space: O(n)
