class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[1] * n for _ in range(m)]

        for i in range(n):
            if obstacleGrid[0][i] == 1:
                for j in range(i, n):
                    paths[0][j] = 0
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                for j in range(i, m):
                    paths[j][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                else:
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
        
        return paths[m - 1][n - 1]