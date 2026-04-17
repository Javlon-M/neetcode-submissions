# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        head = tmp = ListNode()
        remain = 0
        while curr1 or curr2 or remain:
            a, b = 0, 0

            if curr1:
                a = curr1.val
                curr1 = curr1.next
            
            if curr2: 
                b = curr2.val
                curr2 = curr2.next
            
            remain, c = divmod(a + b + remain, 10)

            tmp.next = ListNode(c)
            tmp = tmp.next
        
        return head.next