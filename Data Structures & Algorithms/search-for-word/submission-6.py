class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def backtrack(i: int, x:int, y: int) -> bool:
            if i == len(word):
                return True
            if not (0 <= x < ROWS and 0 <= y < COLS and word[i] == board[x][y] and board[x][y] != "#"):
                return False
            
            board[x][y] = "#"
            res = (backtrack(i + 1, x, y + 1) or
                   backtrack(i + 1, x + 1, y) or
                   backtrack(i + 1, x, y - 1) or
                   backtrack(i + 1, x - 1, y))
            board[x][y] = word[i]
            return res

        for x in range(ROWS):
            for y in range(COLS):
                if backtrack(0, x, y):
                    return True
        
        return False