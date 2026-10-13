from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r: int, c: int) -> int:
            area = 0
            queue = deque([(r, c)])
            grid[r][c] = 0
            while queue:
                cr, cc = queue.popleft()
                area += 1
                for dr, dc in delta:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 0
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area