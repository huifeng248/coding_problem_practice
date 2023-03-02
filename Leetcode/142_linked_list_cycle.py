# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# optimize Solution:
#     # time complexity O(n)
#     # space complexity O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                start = head
                while slow != start:
                    slow = slow.next
                    start = start.next
                return start
        return None
        

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         visited_dict = {}
#         count = 0
#         current = head
#         while current:
#             if current not in visited_dict:
#                 visited_dict[current] = count
#                 count += 1
#                 current = current.next
#             else:
#                 return current
#         return None

#     # time complexity O(n)
#     # space complexity O(n)
