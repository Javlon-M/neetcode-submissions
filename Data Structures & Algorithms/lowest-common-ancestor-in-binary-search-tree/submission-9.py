# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        maxi, mini = max(q.val, p.val), min(q.val, p.val)

        return self.lowest(root, mini, maxi)
    
    def lowest(self, root, mini, maxi):
        if mini <= root.val <= maxi:
            return root

        if root.val > maxi:
            return self.lowest(root.left, mini, maxi)
        
        return self.lowest(root.right, mini, maxi)