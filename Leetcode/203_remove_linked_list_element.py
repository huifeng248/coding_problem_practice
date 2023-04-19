class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(None)
        dummy_head.next = head

        current = head
        prev = dummy_head
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return dummy_head.next

# Time complexity: O(N), it's one pass solution.

# Space complexity: O(1), it's a constant space solution.