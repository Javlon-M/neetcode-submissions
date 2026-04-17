# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs
        self.res = 0
        def countGoodNodes(node, maxi):
            if not node:
                return
            if node.val >= maxi:
                self.res += 1
            
            countGoodNodes(node.left, max(maxi, node.val))
            countGoodNodes(node.right, max(maxi, node.val))
        
        countGoodNodes(root, float("-inf"))
        return self.res