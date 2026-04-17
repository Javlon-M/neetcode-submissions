class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        counts = [[] for i in range(len(nums) + 1)]
        ans = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num, count in freq.items():
            counts[count].append(num)

        for i in range(len(counts) - 1, -1, -1):
            ans += counts[i]
            
            if len(ans) == k:
                break
        
        return ans