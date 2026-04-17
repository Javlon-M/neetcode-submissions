class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        stack = []
        bs = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for p in s:
            if p in ["(", "{", "["]:
                stack.append(p)
            else:
                if len(stack) == 0 or stack.pop() != bs[p]:
                    return False

        return len(stack) == 0