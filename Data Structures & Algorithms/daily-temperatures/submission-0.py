class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        # [1,4,1,2,1,0,0]
        # [(40, j), (28, i)]
        stack = [(temperatures[0], 0)]
        res = [0] * len(temperatures)

        i = 1
        while i < len(temperatures): 
            while stack and stack[-1][0] < temperatures[i]: 
                a, j = stack.pop() 
                res[j] = i - j 
            stack.append((temperatures[i], i))
            i += 1 
        
        return res
        

