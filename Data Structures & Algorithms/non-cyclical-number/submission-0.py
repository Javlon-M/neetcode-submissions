class Solution:
    processed = set()
    def isHappy(self, n: int) -> bool:
        n = str(n)

        if n == "1" or n == "7": return True

        if len(n) == 1:
            if n in self.processed:
                return False
            self.processed.add(n)

        x = 0
        for i in n:
            x += int(i)**2
        
        return self.isHappy(x)
