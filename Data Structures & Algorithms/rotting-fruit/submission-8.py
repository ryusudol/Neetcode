from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()
        fresh_cnt = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_cnt += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        time = 0
        while queue and fresh_cnt > 0:
            time += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_cnt -= 1
                        queue.append((nr, nc))

        return time if fresh_cnt == 0 else -1
