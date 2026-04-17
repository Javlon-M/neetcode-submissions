"""
nums can be empty? no
elements can be negative numbers? yes. -1k to 1k

initial though is like a brute force solution we should find break down from max to min then min will be the answer. it takes O(n) time
optimal approach will be binary search:
1st should compare left most and right most elements 
if left is less than right, then min is in left side, otherwise min is in right side
base case will be if right is equal to left
check every avarage elemt and store min one
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == nums[right]: return nums[left]

            mid = (left + right)//2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]

        