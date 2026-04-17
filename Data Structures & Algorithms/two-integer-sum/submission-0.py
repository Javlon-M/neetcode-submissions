class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        ans = []
        for i in range(len(nums)):
            if nums[i] in dic:
                ans += [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i
        return ans
