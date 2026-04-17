# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        output = [root.val]
        dq = deque([root])

        while dq:
            n = len(dq)
            i = 0
            while i < n:
                node = dq.pop()

                if node.left:
                    dq.appendleft(node.left)

                if node.right:
                    dq.appendleft(node.right)

                i += 1

            if dq:
                output.append(dq[0].val)
        
        return output




        