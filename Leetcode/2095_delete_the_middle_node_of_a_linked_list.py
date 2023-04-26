# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# two passes
# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next: 
#             return None
        
#         list_len = 0
#         current = head
#         while current:
#             current = current.next
#             list_len +=1

#         mid_point = list_len //2
        
#         current = head
#         count = 0
#         while current and count < mid_point-1:
#             current = current.next
#             count += 1

#         current.next = current.next.next

#         return head

# one pass
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        # slow need to record the one before, therefore, fast need to go one step before 
        fast = head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        if slow: slow.next = slow.next.next
        return head
