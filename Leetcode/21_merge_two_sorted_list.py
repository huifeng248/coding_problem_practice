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
    
# Time complexity : O(n+m), Because exactly one of l1 and l2 is incremented on each loop iteration, the while loop runs for a number of iterations equal to the sum of the lengths of the two lists. All other work is constant, so the overall complexity is linear.

# Space complexity : O(1), The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.
    #recursion 
    
    class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
# Time complexity : O(n+m),
# Space complexity : O(n+m),