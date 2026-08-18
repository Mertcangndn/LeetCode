# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
            
        anchor1 = ListNode(0,list1)

        right = anchor1.next
        left = anchor1

        while right != None and list2 != None:
            if list2.val <= right.val:
                left.next = ListNode(list2.val,right)
                list2 = list2.next
                left = left.next
            else:
                left = right
                right = right.next
        
        while list2 != None:
            left.next = ListNode(list2.val)
            left = left.next
            list2 = list2.next

        return anchor1.next