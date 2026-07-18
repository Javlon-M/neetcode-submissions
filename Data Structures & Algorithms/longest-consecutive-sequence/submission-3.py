class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0
        for num in nums:
            if num - 1 not in nums_set:
                leng = 0
                while num + leng in nums_set:
                    leng += 1
                longest = max(longest, leng)
    
        return longest