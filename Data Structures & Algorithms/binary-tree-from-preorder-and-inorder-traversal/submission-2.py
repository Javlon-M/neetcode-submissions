# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        
        def dfs(p, i):
            if not p or not i:
                return None
            
            root = TreeNode(p[0])
            mid = i.index(p[0])
            root.left = dfs(p[1:mid+1], i[:mid])
            root.right = dfs(p[mid + 1:], i[mid + 1:])

            return root

        return dfs(preorder, inorder)


