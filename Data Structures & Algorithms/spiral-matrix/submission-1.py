class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        m, n = len(matrix), len(matrix[0])

        def spiral(t, r, b, l): 
            if not (t < b and l < r): return

            # get every i in the top row
            for i in range(l, r): 
                output.append(matrix[t][i])
            t += 1

            # get every i in the right row
            for i in range(t, b): 
                output.append(matrix[i][r - 1]) 
            r -= 1

            if not (t < b and l < r): return

            # get every i in the bottom row
            for i in range(r - 1, l - 1, -1):
                output.append(matrix[b - 1][i]) 
            b -= 1

            # get every i in the left row
            for i in range(b - 1, t - 1, -1):
                output.append(matrix[i][l]) 
            l += 1

            spiral(t, r, b, l)

        spiral(0, n, m, 0)
        return output