class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited, graph = set(), defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(i, visiting):
            if i in visiting: return

            visiting.add(i)
            for ni in graph[i]:
                if ni in visited: continue
                dfs(ni, visiting)
            
            visited.add(i)
            visiting.remove(i)

        count = 0
        for i in range(n):
            if i in visited: continue

            dfs(i, set())
            count += 1
        
        return count