class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a + b + c = 0

        output = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue

            l, r = i + 1, len(nums) - 1
            while r > l:
                if nums[i] + nums[l] + nums[r] == 0:
                    output.append([nums[i], nums[l], nums[r]])

                    while r > l and nums[l] == nums[l + 1]: l += 1
                    while r > l and nums[r] == nums[r - 1]: r -= 1

                    r -= 1
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

        return output    