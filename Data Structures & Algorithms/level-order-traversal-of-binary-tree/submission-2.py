# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
 
        output = []
        de = deque([root])
        while de:
            children = []
            level = []
            while de:
                node = de.popleft()
                level.append(node.val)
                if node.left:
                    children.append(node.left)
                
                if node.right:
                    children.append(node.right)
                
            if level:
                output.append(level)

            de = deque(children)
        
        return output