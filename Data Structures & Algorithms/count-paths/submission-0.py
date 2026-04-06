class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * n
        
        for _ in range(m - 1, -1, -1):
            cur = [0] * n
            cur[n - 1] = 1
            for i in range(n - 2, -1, -1):
                cur[i] = cur[i + 1] + prev[i]
            prev = cur
            print(cur)
        
        return prev[0]