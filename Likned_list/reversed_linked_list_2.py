#node !!! it becomes a double linked list
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def reverse_list(head):
  prev = dummy_head = Node(None)
#   dummy_head.next = head
  current = head
  while current:
    temp = current.next
    current.next = prev
    prev = current
    current = temp
  return prev

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

temp = reverse_list(a) # f -> e -> d -> c -> b -> a

def print_temp(head):
    while head:
        print(head.val)
        head = head.next
    return "yes"

print(print_temp(temp))

