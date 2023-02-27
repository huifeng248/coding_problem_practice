# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited_dict = {}
        count = 0
        current = head
        while current:
            if current not in visited_dict:
                visited_dict[current] = count
                count += 1
                current = current.next
            else:
                return current
        return None

    # time complexity O(n)
    # space complexity O(n)