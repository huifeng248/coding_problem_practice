class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def sum_list(head):
#   total = 0
#   current = head
  
#   while current is not None:
#     print(total)
#     total += current.val
#     current = current.next
  
#   return total




# def sum_list(head):
#   total = 0 
  
#   if head is None:
#     return total 
#   print("before", total)
#   total += head.val
#   print("after", total)
  
#   return total + sum_list(head.next)

# def sum_list(head):
#   total = [0]
  
#   add_nums(head, total)
  
#   return total[0]

# def add_nums(head, total):
#   if head is None:
#     return total
#   print("before", total)
#   total[0] += head.val
#   print("after", total)
  
#   return add_nums(head.next, total)

def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

print(sum_list(a)) # 19

# solutions
# iterative
def sum_list(head):
  total_sum = 0
  current = head
  while current is not None:
    total_sum += current.val
    current = current.next
  return total_sum
# n = number of nodes
# Time: O(n)
# Space: O(1)
# recursive

def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)
# n = number of nodes
# Time: O(n)
# Space: O(n)
