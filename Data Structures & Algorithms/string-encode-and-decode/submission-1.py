class Solution:
    def encode(self, strs: List[str]) -> str:
        sizes = []

        for s in strs:
            sizes.append(len(s))
        
        ans = ""

        for i in range(len(sizes)):
            ans += str(sizes[i]) + "#" + strs[i]
        
        return ans

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])

            i = j + 1
            j = i + l

            strs.append(s[i:j])
            i = j
        
        return strs
            
