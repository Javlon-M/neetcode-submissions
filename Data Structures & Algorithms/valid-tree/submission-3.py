class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges: return True 
        if n == 1: return False

        visited, graph = set(), defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(i, visiting):
            if i in visiting: 
                return
            
            visiting.add(i)

            for ni in graph[i]:
                if ni in visited: 
                    raise ValueError("")

                dfs(ni, visiting)
            visited.add(i)
            visiting.remove(i)
        
        count = 0
        for i in range(n):
            if i in visited: continue
            
            try:
                dfs(i, set())
            except ValueError:
                return False

            count += 1
        
        return count == 1