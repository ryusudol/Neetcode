class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r: int, c: int) -> bool:
            reach_pac, reach_atl = False, False
            queue = deque([(r, c)])
            visited = set([(r, c)])

            while queue:
                cr, cc = queue.popleft()
                if not reach_pac and cr == 0 or cc == 0:
                    reach_pac = True
                if not reach_atl and cr == ROWS - 1 or cc == COLS - 1:
                    reach_atl = True

                if reach_pac and reach_atl:
                    return True

                for dr, dc in delta:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if heights[cr][cc] >= heights[nr][nc] and (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
            
            return False
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if bfs(r, c):
                    res.append([r, c])
        
        return res