from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pac, atl = [[False] * cols for _ in range(rows)], [[False] * cols for _ in range(rows)]

        def bfs(ocean, start_points):
            queue = deque(start_points)
            for x, y in start_points:
                ocean[x][y] = True
            while queue:
                cur_x, cur_y = queue.popleft()
                for dx, dy in delta:
                    next_x, next_y = cur_x + dx, cur_y + dy
                    if 0 <= next_x < rows and 0 <= next_y < cols:
                        if not ocean[next_x][next_y] and heights[next_x][next_y] >= heights[cur_x][cur_y]:
                            queue.append((next_x, next_y))
                            ocean[next_x][next_y] = True

        pac_starts = [(0, y) for y in range(cols)] + [(x, 0) for x in range(1, rows)]
        atl_starts = [(rows - 1, y) for y in range(cols)] + [(x, cols - 1) for x in range(rows - 1)]

        bfs(pac, pac_starts)
        bfs(atl, atl_starts)

        return [(x, y) for x in range(rows) for y in range(cols) if pac[x][y] and atl[x][y]]