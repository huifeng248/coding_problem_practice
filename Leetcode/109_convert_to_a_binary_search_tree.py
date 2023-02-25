# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # def findMiddle(self, head):
    #     if head is None or head.next is None:
    #         return head
    #     slow = head
    #     fast = head
    #     prev = None
    #     while fast and fast.next:
    #         prev = slow
    #         slow = slow.next 
    #         print("fast", fast.val)
    #         fast = fast.next.next
    #     prev.next = None
    #     print("slow~~", slow.val)
    #     return slow

    # def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    #     if head is None or head.next is None:
    #         return head
    #     mid = self.findMiddle(head)
    #     left = self.sortedListToBST(head)
    #     right = self.sortedListToBST(mid)
    #     head.left = left
    #     head.right = right
    #     return head    
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)
        
        slow = head
        fast = head
        
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next 
            print("fast", fast.val)
            fast = fast.next.next
        prev.next = None
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        
        return node