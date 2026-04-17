class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        
        return heapq.nlargest(k, nums, key=nums.get)