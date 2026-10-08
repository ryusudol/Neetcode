class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()

        def backtrack(i: int, x:int, y: int) -> bool:
            if i == len(word) - 1 and word[i] == board[x][y]:
                return True
            if word[i] != board[x][y]:
                return False

            for dx, dy in delta:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < row and 0 <= next_y < col and (next_x, next_y) not in seen:
                    seen.add((next_x, next_y))
                    res = backtrack(i + 1, next_x, next_y)
                    seen.remove((next_x, next_y))
                    if res:
                        return True

            return False

        for x in range(row):
            for y in range(col):
                seen.add((x, y))
                if backtrack(0, x, y):
                    return True
                seen.remove((x, y))
        
        return False