# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
4,3,5,2,null k = 4
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        dq, node = deque([]), root
        count = 0

        while dq or node:
            while node:
                dq.append(node)
                node = node.left
            
            node = dq.pop()
            count += 1
            if count == k: return node.val

            node = node.right

            