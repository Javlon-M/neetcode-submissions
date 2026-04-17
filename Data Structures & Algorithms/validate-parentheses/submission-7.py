class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        stack = deque([])

        for b in s:
            if b in ["[", "{", "("]:
                stack.append(b)
            elif stack:
                o = stack.pop()
                if b == "]" and o == "[":
                    continue
                elif b == "}" and o == "{":
                    continue
                elif b == ")" and o == "(":
                    continue
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0