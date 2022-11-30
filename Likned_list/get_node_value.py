

# get node value
# Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# get_node_value(a, 2) # 'c'


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value(head, index):
  i = 0 
  current = head

  while current is not None:
    # print("current~~", current.val)
    # if i < index:
    #   current = current.next
    #   i += 1
    # if i == index:
    #   return current.val
    if i == index:
      return current.val
    i += 1
    current = current.next
  
  return None

# def get_node_value(head, index):
  
#   if head is None:
#     return None
#   if index == 0:
#     return head.val
#   return get_node_value(head.next, index-1)
  


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 2)) # 'c'

# solutions
# iterative
def get_node_value(head, index):
  count = 0
  current = head
  while current is not None:
    if count == index:
      return current.val
    
    current = current.next
    count += 1
    
  return None
# n = number of nodes
# Time: O(n)
# Space: O(1)


# recursive
def get_node_value(head, index):
  if head is None:
    return None
  
  if index == 0:
    return head.val
  
  return get_node_value(head.next, index - 1)
# n = number of nodes
# Time: O(n)
# Space: O(n)