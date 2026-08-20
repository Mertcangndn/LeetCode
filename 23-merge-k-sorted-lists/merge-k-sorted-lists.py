# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        anchor = ListNode(0) # Hepsinin toplanacağın ortak linkedlist'in çapası

        for head in lists:

            if head == None:
                continue
    
            left = anchor
            right = anchor.next

            while head != None:

                if right != None:
                    if head.val <= right.val:
                        left.next = ListNode(head.val,right)
                        left = left.next
                        if left == right: right = right.next
                        head = head.next
                    else:
                        left = right
                        right = right.next
                else:
                    left.next = ListNode(head.val,right)
                    left = left.next
                    head = head.next


        return anchor.next