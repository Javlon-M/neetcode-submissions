class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        m, n = len(matrix), len(matrix[0])

        def spiral(t, r, b, l): # 1, 1, 1, 1
            isStop = True
            for i in range(l, r + 1): # 1 2
                isStop = False
                output.append(matrix[t][i]) # [5]
            if isStop: return 

            isStop = True
            for i in range(t + 1, b + 1): # 
                isStop = False
                output.append(matrix[i][r]) #
            if isStop: return 

            isStop = True
            for i in range(r - 1, l - 1, -1): #
                isStop = False 
                output.append(matrix[b][i]) # 
            if isStop: return 

            isStop = True
            for i in range(b - 1, t, -1): # 
                isStop = False
                output.append(matrix[i][l]) # 
            if isStop: return 
            
            spiral(t + 1, r - 1, b - 1, l + 1)

        spiral(0, n - 1, m - 1, 0)
        return output