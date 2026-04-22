class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # i = 0 ... i - 1 & i + 1 ... n
        pre = [1] * len(nums)
        suff = [1] * len(nums)

        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1] # [1, 1, 2, 8]
        
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1] # [48, 24, 6, 1]
        
        output = []
        for i in range(len(nums)):
            output.append(pre[i] * suff[i])

        return output