class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_seen, col_seen = set(), set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_seen:
                        return False
                    row_seen.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in col_seen:
                        return False
                    col_seen.add(board[j][i])
        for i in range(3):
            for j in range(3):
                grid = [row[3*j:3*j+3] for row in board[3*i:3*i+3]]
                flattened_grid = [x for row in grid for x in row]
                seen = set()
                for val in flattened_grid:
                    if val != "." and val in seen:
                        return False
                    seen.add(val)
        return True