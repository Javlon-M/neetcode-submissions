class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            preMap[a].append(b)
        
        visiting = set()
        def dfs(n):
            if n in visiting:
                return False
            
            if preMap[n] == []:
                return True

            visiting.add(n)
            for b in preMap[n]:
                if not dfs(b): return False

            visiting.remove(n)
            preMap[n] = []
            return True

        for n in range(numCourses):
            if not dfs(n): return False
        return True

