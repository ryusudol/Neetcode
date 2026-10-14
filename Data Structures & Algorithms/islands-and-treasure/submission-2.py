from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()
        visited = set()

        def append_cell(r: int, c: int):
            if not (0 <= r < ROWS and 0 <= c < COLS) or (r, c) in visited or grid[r][c] == - 1:
                return
            
            queue.append((r, c))
            visited.add((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    append_cell(r, c)
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                append_cell(r, c + 1)
                append_cell(r + 1, c)
                append_cell(r, c - 1)
                append_cell(r - 1, c)
            dist += 1