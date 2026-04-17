class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # iterate and define all of them O(n)
        # store calculations in one array
        def getDistances():
            distances = []
            for point in points:
                distances.append(math.sqrt(point[0] ** 2 + point[1] ** 2))
            
            return distances
        
        def getMinHeap(distances):
            maxHeap = []

            for i, val in enumerate(distances):
                heapq.heappush(maxHeap, (-val, i))
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)

            return maxHeap
            
        distances = getDistances()

        minHeap = getMinHeap(distances)

        res = []
        for mini in minHeap:
            res.append(points[mini[1]])

        return res