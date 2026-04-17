# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack, node, prev = deque([]), root, None

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()

            if prev:
                if prev.val >= node.val:
                    return False
            prev = node

            node = node.right            


        return True