# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        de = []
        node = root

        while de or node:
            while node:
                de.append(node)
                node = node.left

            node = de.pop()
            if k == 1:
                return node.val
            k -= 1
            node = node.right
        

        
        