# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         current_1 = dummy_head_1 = ListNode(None)
#         current_2 = dummy_head_2 = ListNode(None)
#         count = 1
#         current = head
#         while current:
#             temp = current.next 
#             if count % 2 == 1:
#                 current_1.next = current
#                 current_1 = current_1.next
#                 current_1.next = None
#             else:
#                 current_2.next = current
#                 current_2 = current_2.next
#                 current_2.next = None
            
#             current = temp
#             count += 1
        
#         current_1.next = dummy_head_2.next
#         return dummy_head_1.next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd = head
        even = head.next
        even_head = even
        
        while odd and even and odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return head
