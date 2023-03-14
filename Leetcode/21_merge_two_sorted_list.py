# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print("come here")
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy_head = ListNode(0)
        current1 = list1
        current2 = list2
        current = dummy_head

        while current1 and current2:
            if current1.val <= current2.val:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next
            current = current.next

        # if not current1:
        #     current.next = current2
        # if not current2:
        #     current.next = current1
        current.next = current1 if current1 is not None else current2
        return dummy_head.next