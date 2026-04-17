# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = deque([root])
        
        ans = []
        while level:
            n = len(level)
            nest = []
            for _ in range(n):
                node = level.pop()
                if not node: continue

                nest.append(node.val)

                level.appendleft(node.left)
                level.appendleft(node.right)
            
            if nest:
                ans.append(nest)
        
        return ans

