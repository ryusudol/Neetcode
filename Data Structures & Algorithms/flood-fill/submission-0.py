from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        visited = set([(sr, sc)])
        queue = deque([(sr, sc)])
        delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        original_color = image[sr][sc]

        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            for i in range(4):
                n_r, n_c = r + delta[i][0], c + delta[i][1]
                if 0 <= n_r < m and 0 <= n_c < n:
                    if (n_r, n_c) not in visited and image[n_r][n_c] == original_color:
                        queue.append((n_r, n_c))
                        visited.add((n_r, n_c))
        
        return image