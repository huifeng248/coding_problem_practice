# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        current = head
        tail = head
        m_count = n_count = 1
        while current:
            m_count = 1
            while (current and m_count < m):
                current = current.next
                m_count += 1
            
            tail = current
            # if tail: print("tail", tail.val)
            # break
            
            n_count = 0
            while current and n_count < n+1:
                current = current.next
                n_count += 1
           
            # if current:
            #     print("current", current.val)
           
            if tail:
                tail.next = current
        return head
# time complexity: O(N)
# space complexity: O(1)
 
        
        
    