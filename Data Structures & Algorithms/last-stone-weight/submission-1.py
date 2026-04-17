class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = MaxHeap()

        for stone in stones: # O(n)
            maxHeap.push(stone)
        
        while maxHeap.heapLen() > 1:
            a, b = maxHeap.pop(), maxHeap.pop()
            c = a - b
            
            if c != 0:
                maxHeap.push(c)
        
        return maxHeap.pop()

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def pop(self):
        if not self.heap:
            return 0
        return -heapq.heappop(self.heap)

    def push(self, val):
        heapq.heappush(self.heap, -val)
    
    def heapLen(self):
        return len(self.heap)

