# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        de = deque([root])
        res = [root.val]

        while de:
            children = []
            while de:
                node = de.popleft()
                if node.right:
                    children.append(node.right)
                
                if node.left:
                    children.append(node.left)
            if children:
                res.append(children[0].val)
            de = deque(children)

        return res
