class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        if n == 1: return nums[0]

        nums1 = nums[1:]
        nums2 = nums[:-1]

        print(nums1)
        print(nums2)

        def dfs(i, nums):
            if i >= n - 1: return 0
            
            if i in memo: return memo[i]

            memo[i] = max(nums[i] + dfs(i + 2, nums), dfs(i + 1, nums))
            
            return memo[i]

        ans1 = dfs(0, nums1)
        memo = {} 
        ans2 = dfs(0, nums2)

        return max(ans1, ans2)