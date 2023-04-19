# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# # interation 
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not list1 and not list2:
#             return None
#         if not list1:
#             return list2
#         if not list2:
#             return list1

        # dummy_head = ListNode(None)
        # current = dummy_head
        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         current.next = list1
        #         list1 = list1.next
        #     else:
        #         current.next = list2
        #         list2 = list2.next
            
        #     current = current.next
        
        # if not list1:
        #     current.next = list2
        # if not list2:
        #     current.next = list1
        # return dummy_head.next


# time complexity: O(m+n)
# space complexity: O(1)

# recursion 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2

# time complexity: O(m+n)
# space complexity: O(m+n)





        
