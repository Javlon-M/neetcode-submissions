class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dic = {}
        ans = []

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

            if dic[num] > n // 3:
                ans.append(num)
            
        return list(set(ans))