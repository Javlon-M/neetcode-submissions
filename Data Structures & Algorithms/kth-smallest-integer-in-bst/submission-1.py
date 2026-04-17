# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque([])
        node = root
        prev = None

        while (stack or node) and k:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            if node:
                prev = node.val
                k -= 1
            node = node.right

        return prev