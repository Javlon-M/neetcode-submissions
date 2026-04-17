class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        
        for i, num in enumerate(numbers):
            if num in dic:
                return [dic[num], i + 1]
            
            dic[target - num] = i + 1
        