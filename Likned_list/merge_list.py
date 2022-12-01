class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def merge_lists(head_1, head_2):
  
#   if head_1.val < head_2.val:
#     tail = head_1
#     current_1 = head_1.next
#     current_2 = head_2
#     while current_1 is not None and current_2 is not None:
#       if current_1.val <= current_2.val:
#         tail.next = current_1
#         tail = tail.next
#         current_1 = current_1.next
#       else:
#         tail.next = current_2
#         tail = tail.next
#         current_2 = current_2.next
    
#     if current_1 is not None:
#       tail.next = current_1
#     else: 
#       tail.next = current_2
  
#     return head_1
  
#   if head_1.val >= head_2.val:
#     tail = head_2
#     current_2 = head_2.next
#     current_1 = head_1
#     while current_1 is not None and current_2 is not None:
#       if current_1.val <= current_2.val:
#         tail.next = current_1
        
#         tail = tail.next
#         current_1 = current_1.next
#       else:
#         tail.next = current_2
#         tail = tail.next
#         current_2 = current_2.next
    
#     if current_1 is not None:
#       tail.next = current_1
#     else: 
#       tail.next = current_2
  
#   return head_2
    
# def merge_lists(head_1, head_2):
#   print("show !!!")
#   if head_1 is None and head_2 is None:
#     return None
  
#   if head_1 is None:
#     return head_2
  
#   if head_2 is None:
#     return head_1
    
#   if head_1.val <= head_2.val:
#     next_1 = head_1.next
#     head_1.next = merge_lists(next_1, head_2)
#     return head_1
#   else:
#     next_2 = head_2.next 
#     head_2.next = merge_lists(head_1, next_2)
#     return head_2

def merge_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  
  current_1 = head_1
  current_2 = head_2
  while current_1 is not None and current_2 is not None:
    if current_1.val < current_2.val:
      tail.next = current_1
      tail = tail.next
      current_1 = current_1.next

    else:
      tail.next = current_2
      tail = tail.next
      current_2 = current_2.next
  
  
  if current_1 is not None:
    tail.next = current_1
  if current_2 is not None:
    tail.next = current_2
  return dummy_head.next
      
      
# 1 -> 8 -> 9 -> 10
       
  
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 6 -> 8 -> 9 -> 25

print(merge_lists(a, q))
      

# solutions
# iterative
def merge_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  current_1 = head_1
  current_2 = head_2
  
  while current_1 is not None and current_2 is not None:
    if current_1.val < current_2.val:
      tail.next = current_1
      current_1 = current_1.next
    else:
      tail.next = current_2
      current_2 = current_2.next
    tail = tail.next
  
  if current_1 is not None: tail.next = current_1
  if current_2 is not None: tail.next = current_2
    
  return dummy_head.next
# n = length of list 1
# m = length of list 2
# Time: O(min(n, m))
# Space: O(1)

    
# recursive
def merge_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None
  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1
  if head_1.val < head_2.val:
    next_1 = head_1.next
    head_1.next = merge_lists(next_1, head_2)
    return head_1
  else:
    next_2 = head_2.next
    head_2.next = merge_lists(head_1, next_2)
    return head_2
# n = length of list 1
# m = length of list 2
# Time: O(min(n, m))
# Space: O(min(n, m))
    
    
      
    
    

