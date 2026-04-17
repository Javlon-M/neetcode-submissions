class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            dic = set()
            for r in row:
                if r == ".": continue
                if r in dic: return False
                dic.add(r)
        
        for col in zip(*board):
            dic = set()
            for c in col:
                if c == ".": continue
                if c in dic: return False
                dic.add(c)
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] == ".": continue
                    if board[row][col] in seen: return False
                    seen.add(board[row][col])
        
        return True
