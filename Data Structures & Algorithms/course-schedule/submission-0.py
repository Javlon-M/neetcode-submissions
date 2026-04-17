class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited, graph = set(), defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        def dfs(i, visiting):
            if i in visited:
                return

            visiting.add(i)
            for ni in graph[i]:
                if ni in visiting:
                    raise ValueError("Cycle detected")
                
                dfs(ni, visiting)

            visiting.remove(i)
            visited.add(i)

        for i in range(numCourses):
            try:
                dfs(i, set())
            except ValueError:
                return False
            
        return True
