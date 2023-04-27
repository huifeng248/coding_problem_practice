# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# first solution: O(n) time and O(n) space
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        reversed_arr = arr[::-1]
        return arr == reversed_arr


# optimize solution: O(n) time and O(1) space
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

#Could you do it in O(n) time and O(1) space?
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        list_len = 0
        current = head
        while current:
            list_len += 1
            current = current.next
        
        mid = list_len //2
        slow = fast = head
        for i in range(mid):
            fast = fast.next
        fast = self.reversed_list(fast)

        while fast:
            # print("fast", fast.val)
            if fast.val == slow.val:
                fast = fast.next
                slow = slow.next
            else:
                return False
        return True
    
    def reversed_list(self, head):
        if not head:
            return None
        prev = dummy_head = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

            

