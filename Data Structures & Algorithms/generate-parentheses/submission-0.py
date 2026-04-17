class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(o, c, path):
            if o < c or o > n: return

            if o + c == 2 * n:
                res.append(path)
                return
            
            generate(o + 1, c, path + "(")
            generate(o, c + 1, path + ")")


        generate(0, 0, "")
        return res