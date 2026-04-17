class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = 0
        
        for i in nums:
            if i - 1 not in s:
                count = 1
                while i + 1 in s:
                    count += 1
                    i += 1
                
                maxi = max(count, maxi)
        
        return maxi