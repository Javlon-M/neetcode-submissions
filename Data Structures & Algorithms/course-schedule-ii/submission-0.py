class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited, graph = set(), defaultdict(list)
        for u, w in prerequisites:
            graph[u].append(w)
        
        ans = []
        def dfs(i, visiting):
            if i in visiting: 
                raise ValueError("Impossible")
            
            visiting.add(i)

            for ni in graph[i]:
                if ni in visited: continue

                dfs(ni, visiting)
            
            ans.append(i)
            visiting.remove(i)
            visited.add(i)
        
        for i in range(numCourses):
            if i in visited: continue

            try:
                dfs(i, set())
            except ValueError:
                return []
        
        return ans