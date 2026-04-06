class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n - 1) + f(n - 2)
        if n <= 2:
            return n
        memo = {1: 1, 2: 2}
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]