class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = [False] * n
        def dfs(i):
            for j in adj[i]:
                if not visit[j]:
                    visit[j] = True
                    dfs(j)
                    
        res = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                res += 1

        return res

