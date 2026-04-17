class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])

        costs = {}
        for i in range(1, n + 1):
            costs[i] = float("inf")
        costs[k] = 0
        
        heap = [(0, k)]
        visited = set()

        while heap:
            cost, node = heapq.heappop(heap)

            if node in visited: continue

            visited.add(node)

            neighbors = graph[node]
            for u, w in neighbors:
                if u in visited: continue

                newCost = cost + w
                if newCost < costs[u]:
                    costs[u] = newCost
                    heapq.heappush(heap, (newCost, u))
        
        maxCost = max(costs.values())
        return maxCost if maxCost != float("inf") else -1
