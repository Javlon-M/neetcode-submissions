class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) # 3, 4

        def find(row): # 2
            l, r = 0, n - 1 # 0, 3
            while l <= r: # 1 <= 0
                m = (l + r)//2 # 0
                if matrix[row][m] == target: # 14 == 15
                    return True
                elif matrix[row][m] > target: # 14 > 15
                    r = m - 1 # 0
                else:
                    l = m + 1 # 1
            return False

        t, b = 0, m - 1 # 0, 2
        while t <= b: # O(m) # 2 <= 2
            m = (t + b)//2 # 2

            if matrix[m][0] <= target <= matrix[m][-1]: # 14 <= 15 <= 40
                return find(m) # O(n)
            elif matrix[m][0] > target:
                b = m - 1
            else:
                t = m + 1

        return False # O(m*n)