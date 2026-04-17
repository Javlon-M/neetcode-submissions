# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        dq = deque([])
        prev = None
        node = root

        while dq or node:
            while node:
                dq.append(node)
                node = node.left
            
            node = dq.pop()

            if prev and prev.val >= node.val:
                return False
            prev = node
            node = node.right
        
        return True