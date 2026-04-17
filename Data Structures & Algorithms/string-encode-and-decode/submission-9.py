class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs: # "we","say",":","yes"
            output += str(len(s)) + "#" + s

        return output

    def decode(self, s: str) -> List[str]:
        output = []

        def build(i, l):
            tmp = ""
            j = 0
            while j < l and i < len(s):
                tmp += s[i]
                i += 1
                j += 1
            
            return tmp, i

        i = 0
        l = ""
        while i < len(s):  # "2#we3#say1#:3#yes"
            if s[i] == "#" and l:
                tmp, i = build(i + 1, int(l))
                output.append(tmp)
                l = ""
            else:
                l += s[i]
                i += 1

        return output