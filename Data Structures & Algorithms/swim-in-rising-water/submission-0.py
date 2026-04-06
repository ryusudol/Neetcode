import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        costs = {}
        pq = [(grid[0][0], 0, 0)]

        while pq:
            cur_t, x, y = heapq.heappop(pq)
            if (x, y) not in costs:
                costs[(x, y)] = cur_t
                for dx, dy in delta:
                    n_x, n_y = x + dx, y + dy
                    if 0 <= n_x < ROWS and 0 <= n_y < COLS:
                        n_cost = max(cur_t, grid[n_x][n_y])
                        heapq.heappush(pq, (n_cost, n_x, n_y))
        
        return costs[(ROWS - 1, COLS - 1)]