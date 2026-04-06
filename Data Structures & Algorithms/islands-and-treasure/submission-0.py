from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

        def bfs(x, y):
            queue = deque([(0, x, y)])
            visited = [[False] * col for _ in range(row)]
            visited[x][y] = True
            while queue:
                dist, cur_x, cur_y = queue.popleft()
                for i in range(4):
                    next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                    if 0 <= next_x < row and 0 <= next_y < col:
                        if grid[next_x][next_y] != -1 and not visited[next_x][next_y]:
                            queue.append((dist + 1, next_x, next_y))
                            grid[next_x][next_y] = min(grid[next_x][next_y], dist + 1)
                            visited[next_x][next_y] = True

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    bfs(i, j)