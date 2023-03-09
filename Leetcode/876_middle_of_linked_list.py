# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow 

#[1, 2, 3]
#[1, 2, 3, 4]
# # time complexity: O(N)
# # space complexity: O(1)

# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
        
#         arr = []
#         current = head
#         while current:
#             arr.append(current)
#             current = current.next
        
#         if len(arr) % 2 == 0:
#             mid = (len(arr) / 2)
            
#         else:
#             mid = len(arr)//2
        
#         return arr[int(mid)]

# # time complexity: O(N)
# # space complexity: O(N)