from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        
        queue = deque([(1, 0, 0)])
        delta = [(1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        while queue:
            dist, x, y = queue.popleft()
            if x == y == len(grid) - 1:
                return dist
            for i in range(8):
                n_x, n_y = x + delta[i][0], y + delta[i][1]
                if 0 <= n_x < len(grid) and 0 <= n_y < len(grid) and grid[n_x][n_y] == 0:
                    queue.append((dist + 1, n_x, n_y))
                    grid[n_x][n_y] = 1
        
        return -1