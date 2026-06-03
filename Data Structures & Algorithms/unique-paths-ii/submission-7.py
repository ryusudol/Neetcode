class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n

        for idx, val in enumerate(obstacleGrid[0]):
            if val == 0: dp[idx] = 1
            else: break

        for i in range(1, m):
            if obstacleGrid[i][0] == 1: dp[0] = 0
            for j in range(1, n):
                dp[j] = (dp[j] + dp[j - 1]) if obstacleGrid[i][j] == 0 else 0
        
        return dp[-1]