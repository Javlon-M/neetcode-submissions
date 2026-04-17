class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []

        for s in operations:
            if s == "+":
                a = arr[-1] + arr[-2]
                arr.append(a)
            elif s == "C":
                arr.pop()
            elif s == "D":
                a = arr[-1]*2
                arr.append(a)
            else:
                arr.append(int(s))
        
        return sum(arr)