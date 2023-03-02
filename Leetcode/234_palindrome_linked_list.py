# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
    
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        #cut it
        slow.next = None

        reversed_second = self.reversed_list(temp)
        # print("reversed_second", reversed_second)
        return self.compare(head, reversed_second)

    def compare(self, head, second):
        current_a = head
        current_b = second
        while current_b:
            if current_a.val != current_b.val:
                return False
            
            current_a = current_a.next
            current_b = current_b.next
        return True


    def reversed_list(self, head):
        current = head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

            

            

