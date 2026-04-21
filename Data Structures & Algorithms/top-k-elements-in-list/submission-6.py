class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        output = []
        bucket = [[] for _ in range(len(nums) + 1)] 
        
        for key in count:
            bucket[count[key]].append(key)

        for i in range(len(bucket) - 1, 0, -1):
            output = output + bucket[i]

            if len(output) == k:
                return output

        return output