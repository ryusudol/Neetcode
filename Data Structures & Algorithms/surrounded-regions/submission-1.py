from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        surrounded = [[True] * cols for _ in range(rows)]
        starts = (
            [(0, y) for y in range(cols) if board[0][y] == 'O'] +
            [(x, 0) for x in range(1, rows) if board[x][0] == 'O'] +
            [(rows - 1, y) for y in range(1, cols) if board[rows - 1][y] == 'O'] +
            [(x, cols - 1) for x in range(1, rows - 1) if board[x][cols - 1] == 'O']
        )
        
        queue = deque(starts)
        for x, y in starts:
            surrounded[x][y] = False
        while queue:
            cur_x, cur_y = queue.popleft()
            for dx, dy in delta:
                next_x, next_y = cur_x + dx, cur_y + dy
                if 0 < next_x < rows - 1 and 0 < next_y < cols - 1:
                    if board[next_x][next_y] == 'O' and surrounded[next_x][next_y]:
                        queue.append((next_x, next_y))
                        surrounded[next_x][next_y] = False
        
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == 'O' and surrounded[x][y]:
                    board[x][y] = 'X'