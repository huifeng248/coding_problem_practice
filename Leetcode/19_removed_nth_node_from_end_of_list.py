# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# one pass
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # thoughs: there are two pointers, and fast - slow = n. when fast reach the end, slow
        # would the previous of n, and will skip the next and connect the next two.
        slow = fast = head
        for i in range(n):
            fast = fast.next
        # print("val", fast.val)
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        # print("vall", fast.val, slow.val)
        slow.next = slow.next.next
    
        return head 

# time complexity: O(n)

# space complexity:O(1)
        
        
        



