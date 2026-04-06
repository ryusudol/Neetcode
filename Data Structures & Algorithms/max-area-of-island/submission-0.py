class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        row, col = len(grid), len(grid[0])
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

        def bfs(x, y):
            area = 0
            grid[x][y] = 0
            queue = deque([(x, y)])
            while queue:
                cur_x, cur_y = queue.popleft()
                area += 1
                for i in range(4):
                    next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                    if 0 <= next_x < row and 0 <= next_y < col and grid[next_x][next_y] == 1:
                        queue.append((next_x, next_y))
                        grid[next_x][next_y] = 0
            return area
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))
        
        return max_area