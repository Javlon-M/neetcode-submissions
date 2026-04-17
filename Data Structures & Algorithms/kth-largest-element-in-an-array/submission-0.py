class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negative = []
        for num in nums: # O(n)
            heapq.heappush(negative, -num)

        num = 0
        while k > 0: # O(k)
            num = heapq.heappop(negative)
            k -= 1
        
        return -num