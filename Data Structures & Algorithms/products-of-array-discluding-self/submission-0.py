class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product1 = [1] * (n + 1)
        product2 = [1] * (n + 1)

        for i in range(1, n + 1):
            product1[i] = product1[i - 1] * nums[i - 1]
            product2[n - i] = product2[n - i + 1] * nums[n - i]
        

        for i in range(n):
            nums[i] = product1[i] * product2[i + 1]
        
        return nums