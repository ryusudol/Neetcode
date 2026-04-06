from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rotten_pos = []
        fresh_cnt, time = 0, 0

        def bfs(pos):
            nonlocal time, fresh_cnt
            queue = deque(pos)
            while queue:
                cur_time, cur_x, cur_y = queue.popleft()
                time = max(time, cur_time)
                for d in delta:
                    next_x, next_y = cur_x + d[0], cur_y + d[1]
                    if 0 <= next_x < ROWS and 0 <= next_y < COLS and grid[next_x][next_y] == 1:
                        grid[next_x][next_y] = 2
                        fresh_cnt -= 1
                        queue.append((cur_time + 1, next_x, next_y))
        
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 2:
                    rotten_pos.append((0, x, y))
                elif grid[x][y] == 1:
                    fresh_cnt += 1

        bfs(rotten_pos)
        return time if fresh_cnt == 0 else -1