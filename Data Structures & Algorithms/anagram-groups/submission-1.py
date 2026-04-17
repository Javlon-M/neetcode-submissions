class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        ans = []
        for word in strs:
            dic["".join(sorted(word))].append(word)
        
        return list(dic.values())
