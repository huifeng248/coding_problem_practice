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
        
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy_head = ListNode(None)
        dummy_head.next = head
        fast= slow = head
        for i in range(n):
            fast = fast.next 
        # fast is None, means n == lengh of linked list. just return head.next 
        if not fast: 
            return head.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        if slow.next:
            slow.next = slow.next.next
        else:
            slow.next = None

        return dummy_head.next



# time complexity: O(n)

# space complexity:O(1)
        