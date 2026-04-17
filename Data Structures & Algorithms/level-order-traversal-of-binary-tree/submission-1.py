# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        res = []
        dq = deque([root]) # [1]

        while dq:  # [4,5,6,7]
            n = len(dq) # 4
            level = []
            for i in range(n): # 4
                node = dq.popleft() # 7

                level.append(node.val) # [4,5,6,7]

                if node.left:
                    dq.append(node.left) # []
                if node.right:
                    dq.append(node.right) # []

            res.append(level) # [[1], [2,3], [4,5,6,7]]
        
        return res