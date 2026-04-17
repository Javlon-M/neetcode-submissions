class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] 

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, c in count.items():
            freq[c].append(num)
        
        ans = []
        for i in range(len(freq) - 1, -1, -1):
            if freq[i]:
                ans += freq[i]

            if len(ans) == k:
                return ans