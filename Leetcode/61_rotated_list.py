# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # need to walk through the total linked list and get the total number of node
        # total - k is the one that need to point to none, and the second half till end need to point to head 
        # return the second half head.
        if k == 0:
            return head
        if head is None:
            return None
        if head.next is None:
            return head
        arr = [head.val]
        current = head 
        while current.next:
            arr.append(current.next.val)
            current = current.next
        current.next = head
        total_len = len(arr)
        
        move_step = k % total_len
        print("move_step", move_step)
        if move_step == 0:
            return head
        
        new_tail = head
        for i in range(total_len - move_step -1):
            new_tail = new_tail.next
            print("i", i)
        print(new_tail.val)
        
        answer = new_tail.next
        new_tail.next = None
        return answer


# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
#         if not head:
#             return None
        
#         lastElement = head
#         length = 1
        # # get the length of the list and the last node in the list
        # while ( lastElement.next ):
        #     lastElement = lastElement.next
        #     length += 1

        # # If k is equal to the length of the list then k == 0
        # # ElIf k is greater than the length of the list then k = k % length
        # k = k % length
            
        # # Set the last node to point to head node
        # # The list is now a circular linked list with last node pointing to first node
        # lastElement.next = head
        
        # # Traverse the list to get to the node just before the ( length - k )th node.
        # # Example: In 1->2->3->4->5, and k = 2
        # #          we need to get to the Node(3)
        # tempNode = head
        # for _ in range( length - k - 1 ):
        #     tempNode = tempNode.next
        
        # # Get the next node from the tempNode and then set the tempNode.next as None
        # # Example: In 1->2->3->4->5, and k = 2
        # #          tempNode = Node(3)
        # #          answer = Node(3).next => Node(4)
        # #          Node(3).next = None ( cut the linked list from here )
        # answer = tempNode.next
        # tempNode.next = None
        
        # return answer