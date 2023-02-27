# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def build_dict(headA):
            current = headA
            visited = set()
            count = 0
            while current:

                visited.add(current)
                current = current.next
            return visited
        
        visited = build_dict(headA)
        currnt_b = headB
        while currnt_b:
            if currnt_b in visited:
                return currnt_b
            else:
                currnt_b = currnt_b.next
        return None
