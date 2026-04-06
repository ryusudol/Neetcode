class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        row, col = len(grid), len(grid[0])
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

        def bfs(x, y):
            grid[x][y] = "0"
            queue = deque([(x, y)])
            while queue:
                cur_x, cur_y = queue.popleft()
                for i in range(4):
                    next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                    if 0 <= next_x < row and 0 <= next_y < col:
                        if grid[next_x][next_y] == "1":
                            queue.append((next_x, next_y))
                            grid[next_x][next_y] = "0"
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    num_islands += 1
        
        return num_islands



        # island_count = 0
        # row, col = len(grid), len(grid[0])
        # visited = [[False for _ in range(col)] for _ in range(row)]
        # dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

        # def bfs(x, y):
        #     visited[x][y] = True
        #     queue = deque([(x, y)])
        #     while queue:
        #         cur_x, cur_y = queue.popleft()
        #         for i in range(4):
        #             next_x, next_y = cur_x + dx[i], cur_y + dy[i]
        #             if 0 <= next_x < row and 0 <= next_y < col:
        #                 if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
        #                     queue.append((next_x, next_y))
        #                     visited[next_x][next_y] = True

        # for i in range(row):
        #     for j in range(col):
        #         if not visited[i][j] and grid[i][j] == '1':
        #             bfs(i, j)
        #             island_count += 1

        # return island_count