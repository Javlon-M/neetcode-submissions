class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def calculate(a, b, operator):
            if operator == "+":
                return a + b
            elif operator == "-":
                return a - b
            elif operator == "*":
                return a * b
            else:
                return int(a / b)

        for token in tokens: 
            if token in ["+", "-", "*", "/"]:
                b = stack.pop() 
                a = stack.pop() 
                tmp = calculate(a, b, token) 
                stack.append(tmp)
            else:
                stack.append(int(token))

        return stack[0]