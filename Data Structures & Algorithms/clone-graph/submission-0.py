"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        
        nodes, visited = {}, set()

        def dfs(curr):
            if curr in visited: return
            visited.add(curr)

            dump = Node(curr.val)
            nodes[curr] = dump
            for n in curr.neighbors:
                dfs(n)

            for n in curr.neighbors:
                dump.neighbors.append(nodes[n])

        dfs(node)

        return nodes[node]
