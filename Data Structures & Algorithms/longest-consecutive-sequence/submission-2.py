class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        for num in s:
            if (num - 1) in s:
                continue

            leng = 0
            while num + leng in s:
                leng += 1
            longest = max(leng, longest) 

        return longest