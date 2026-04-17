class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return ""

        if strs == [""]: return ";#"

        return ";#".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "": return []
        if s == ";#": return [""]

        output = []
        string = ""
        for i in range(len(s)):
            if s[i] == "#" and i - 1 >= 0 and s[i - 1] == ";":
                continue

            if s[i] == ";" and i + 1 < len(s) and s[i + 1] == "#":
                output.append(string)
                string = ""
                continue
            
            string += s[i]

        output.append(string)    
        return output
