# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic = {}
        preorder = deque(preorder)

        for i in range(len(inorder)):
            dic[inorder[i]] = i
        
        def dfs(start, end):
            if start > end: return None

            node = TreeNode(preorder.popleft())
            mid = dic[node.val]

            node.left = dfs(start, mid - 1)
            node.right = dfs(mid + 1, end)

            return node

        return dfs(0, len(inorder) - 1)



