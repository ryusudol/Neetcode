from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(ocean, starts):
            q = deque(starts)
            for r, c in starts:
                ocean[r][c] = True
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        ocean[nr][nc] = True
                        q.append((nr, nc))

        pac_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(1, rows)]
        atl_starts = [(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows-1)]

        bfs(pac, pac_starts)
        bfs(atl, atl_starts)

        return [[r, c] for r in range(rows) for c in range(cols) if pac[r][c] and atl[r][c]]

# from collections import deque

# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         ROWS, COLS = len(heights), len(heights[0])
#         delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         ans = []

#         def bfs(x, y):
#             pac, atl = False, False
#             visited = [[False] * COLS for _ in range(ROWS)]
#             visited[x][y] = True
#             queue = deque([(x, y)])
#             while queue:
#                 cur_x, cur_y = queue.popleft()
#                 if cur_x == 0 or cur_y == 0:
#                     pac = True
#                 if cur_x == ROWS - 1 or cur_y == COLS - 1:
#                     atl = True
#                 if pac and atl:
#                     ans.append([x, y])
#                     return
#                 for d in delta:
#                     next_x, next_y = cur_x + d[0], cur_y + d[1]
#                     if 0 <= next_x < ROWS and 0 <= next_y < COLS and not visited[next_x][next_y]:
#                         if heights[next_x][next_y] <= heights[cur_x][cur_y]:
#                             queue.append((next_x, next_y))
#                             visited[next_x][next_y] = True
        
#         for x in range(ROWS):
#             for y in range(COLS):
#                 bfs(x, y)

#         return ans