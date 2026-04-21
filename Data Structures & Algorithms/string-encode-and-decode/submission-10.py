class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            output += str(len(s)) + "#" + s

        return output

    def decode(self, s: str) -> List[str]:
        output = []

        def build(i, n):
            j = 0
            word = ""
            while j < n and i < len(s):
                word += s[i]
                i += 1
                j += 1
            
            return word, i

        i = 0
        tmp = ""
        while i < len(s):
            if s[i] == "#" and tmp:
                word, i = build(i + 1, int(tmp))
                output.append(word)
                tmp = ""
            else:
                tmp += s[i]
                i += 1
        
        return output