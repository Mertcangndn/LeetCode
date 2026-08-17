# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        
        back = temp
        front = temp
        
        for i in range(n + 1):
            front = front.next
            
        while front is not None:
            back = back.next
            front = front.next

        back.next = back.next.next
        
        return temp.next