class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

#  in_place reverse means changing the direction
# use prev and next variable/pointers
# def reverse_list(head):
#   previous = None
#   current = head

#   while current is not None:
# #     save current.next into a variable next in order not to lose it, 
# # as we need to reassign the current.next the new value and position (of the previous).
#     next = current.next
# #   change the direction of the current pointer 
#     current.next = previous
  
# # move the pointer to next node
#     previous = current
#     current = next


#   return previous

def reverse_list(head, prev = None):
  if head is None:
    return prev

  #   save head.next in a variable
  next = head.next
#   set the reverse direction
  head.next = prev
  return reverse_list(next, head)


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

reverse_list(a) # f -> e -> d -> c -> b -> a


# solutions
# iterative
def reverse_list(head):
  prev = None
  current = head
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev
# n = number of nodes
# Time: O(n)
# Space: O(1)
# recursive

def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)
# n = number of nodes
# Time: O(n)
# Space: O(n)
    
  
