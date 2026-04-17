class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        ans = []
        for word in strs:
            dic["".join(sorted(word))].append(word)
        
        for word in dic:
            ans.append(dic[word])
        
        return ans
