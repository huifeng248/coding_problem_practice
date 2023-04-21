# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# using arr
# class Solution:
#     def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if not head:
#             return None
        
#         current = head
#         prev = ListNode(None)
#         arr = []
#         while current:
#             arr.append(current)
#             prev = current
#             current = current.next
        
#         if k == 0 or k == len(arr):
#             temp = prev.val 
#             prev.val = head.val
#             head.val = temp
#             return head

#         if k == len(arr)/2:
#             swap1, swap2= arr[k-1],arr[k]
#         else:
#             swap1= arr[k-1]
#             swap2= arr[len(arr)-k]
#         temp = swap1.val
#         swap1.val = swap2.val
#         swap2.val = temp
#         return head
# time complexity: O(N)
# space complexity: O(N)

# using two pointers

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        swap1 = swap2 = head
        for i in range(1, k):
            swap1 = swap1.next
        
        end = swap1
        while end and end.next:
            swap2 = swap2.next
            end = end.next
        
        # print(end.val) end is already the last node, cause of the line"end=end.next"
        if swap1 != swap2:
            swap1.val, swap2.val = swap2.val, swap1.val
        
        return head

        

        
        
 
