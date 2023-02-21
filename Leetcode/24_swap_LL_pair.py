# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        first_Node = head
        second_node = head.next

        # assuming the remaining is working, the temp is the next nodes need to attached to the first_Node

        temp = self.swapPairs(second_node.next)
        first_Node.next = temp
        second_node.next = first_Node
        return second_node

# Time Complexity: O(N), the size of the linked list.
# Space Complexity: O(N), stack space utilized for recursion.


            