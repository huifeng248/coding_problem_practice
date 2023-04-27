# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, list_1, list_2):
        tail = dummy_head = ListNode(None)
        while list_1 and list_2:
            if list_1.val <= list_2.val:
                tail.next = list_1
                list_1 = list_1.next
            else:
                tail.next = list_2
                list_2 = list_2.next
            
            tail = tail.next
        
        # tail.next = list_1 if not list_2 else list_2
        if list_1:
            tail.next = list_1
        
        if list_2:
            tail.next = list_2
        return dummy_head.next
    
    # leetcode problem 876
    def get_mid(self, head):
        if not head or not head.next:
            return head
        prev_slow = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            if prev_slow is None:
                prev_slow = head
            else:
                prev_slow = prev_slow.next
        
        # have to cut the linked list into half
        slow = prev_slow.next
        prev_slow.next = None

        return slow

   
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
        
#         mid_point = self.get_mid(head)
#         left = self.sortList(head)
#         right = self.sortList(mid_point)
#         return self.merge(left, right)
    
    # def merge(self, list_1, list_2):
    #     current = dummy_head = ListNode(None)
        
    #     while list_1 and list_2:
    #         if list_1.val <= list_2.val:
    #             current.next = list_1
    #             list_1 = list_1.next
    #         else:
    #             current.next = list_2
    #             list_2 = list_2.next 
            
    #         current = current.next
        
    #     current.next = list_1 if list_1 else list_2
    #     return dummy_head.next
    
        
    # def get_mid(self, head):
    #     prev = None
    #     fast = head
    #     while fast and fast.next:
    #         if prev is None:
    #             prev = head
    #         else:
    #             prev = prev.next
            
    #         fast = fast.next.next
        
    #     slow = prev.next
    #     prev.next = None
    #     return slow


# time complexity: O(n(logn)), split takes O(log(n)) and merge take n
# space complexity: O(log(n)),  where nnn is the number of nodes in linked list. Since the problem is recursive, we need additional space to store the recursive call stack. The maximum depth of the recursion tree is log⁡(n)

