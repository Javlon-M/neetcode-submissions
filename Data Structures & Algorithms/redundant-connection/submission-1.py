class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
    
            def find(self, i):
                if self.parent[i] == i:
                    return i
                return self.find(self.parent[i])
    
            def unite(self, i, j):
                irep = self.find(i)
                
                jrep = self.find(j)
                self.parent[irep] = jrep
            
        uf = UnionFind(len(edges) + 1)

        res = []
        for edge in edges:
            [a, b] = edge

            if uf.find(a) == uf.find(b):
                res = [a, b]
                continue
            uf.unite(a, b)

        return res
