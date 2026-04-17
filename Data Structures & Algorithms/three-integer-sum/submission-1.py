class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            a = nums[i]
            if i > 0 and a == nums[i - 1]: continue

            l, r = i + 1, n - 1

            while r > l:
                b = nums[l]
                c = nums[r]

                if a + b + c == 0:
                    ans.append([a, b, c])

                    while r > l and nums[l] == nums[l + 1]: l += 1
                    while r > l and nums[r] == nums[r - 1]: r -= 1

                    r -= 1
                    l += 1
                elif a + b + c > 0:
                    r -= 1
                else:
                    l += 1
        
        return ans