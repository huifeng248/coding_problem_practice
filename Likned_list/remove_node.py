class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def remove_node(head, target_val):
  current = head 
  prev = head
  if head.val == target_val:
    return head.next
  
  while current is not None:
    if current.val != target_val:
      prev = current
      current = current.next
    else:
      prev.next = current.next
      return head

# remove node
# Write a function, remove_node, that takes in the head of a linked list and a target value as arguments. The function should delete the node containing the target value from the linked list and return the head of the resulting linked list. If the target appears multiple times in the linked list, only remove the first instance of the target in the list.

# Do this in-place.

# You may assume that the input list is non-empty.

# You may assume that the input list contains the target.

# test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

remove_node(a, "c")
# a -> b -> d -> e -> f


# remove all the node which is the same with the target value.
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def remove_node(head, target_val):
  current = head 
  prev = head
  if head.val == target_val:
    return head.next
  
  while current is not None:
    if current.val != target_val:
      prev = current
      current = current.next
    else:
      prev.next = current.next
      prev = current
      current = current.next
  return head

def remove_node(head, target_val):
  if head is None:
    return None
  if head.val == target_val:
    return head.next
  
  head.next = remove_node(head.next, target_val)
  return head

# iterative
def remove_node(head, target_val):
  if head.val == target_val:
    return head.next

  current = head
  prev = None
  while current is not None:
    if current.val == target_val:
      prev.next = current.next
      break
    prev = current
    current = current.next
  return head
# n = number of nodes
# Time: O(n)
# Space: O(1)
# recursive
def remove_node(head, target_val):
  if head is None:
    return None

  if head.val == target_val:
    return head.next

  head.next = remove_node(head.next, target_val)
  return head
# n = number of nodes
# Time: O(n)
# Space: O(n)