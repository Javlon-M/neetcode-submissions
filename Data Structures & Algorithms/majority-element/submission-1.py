class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        vote = 0

        for num in nums:
            if vote == 0:
                candidate = num
                vote = 1
            else:
                if candidate == num:
                    vote += 1
                else:
                    vote -= 1
        
        return candidate