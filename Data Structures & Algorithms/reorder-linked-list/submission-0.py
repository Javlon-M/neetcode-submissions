# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = ListNode(None)

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        slow.next = None
        while temp:
            node = ListNode(temp)
            node.next = stack
            stack = node
            temp = temp.next

        curr = head
        while head and stack.val:
            node = stack.val
            stack = stack.next

            nxt = curr.next
            curr.next = node
            node.next = nxt
            curr = nxt
        
            



