# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        mini, maxi = min(q.val, p.val), max(q.val, p.val)
        
        def lowest(node):
            res = node

            if mini <= node.val <= maxi:
                res = node
            elif mini < node.val:
                res = lowest(node.left)
            else:
                res = lowest(node.right)

            return res
        
        return lowest(root)