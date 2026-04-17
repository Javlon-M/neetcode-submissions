class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = set()

        for i in range(n):
            for j in range(i + 1, n):
                k = j + 1
                l = n - 1

                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        output.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif s < target:
                        k += 1
                    else:
                        l -= 1
        
        return list(output)