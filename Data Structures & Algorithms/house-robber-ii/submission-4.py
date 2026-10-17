class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return max(nums)

        dp = [[0 for _ in range(len(nums))] for _ in range(2)]
        dp[0][0], dp[1][1] = nums[0], nums[1]

        for i in range(2, n):
            if i != n - 1:
                dp[0][i] = max(dp[0][i - 2], dp[0][i - 3] if i >= 3 else 0) + nums[i]
            dp[1][i] = max(dp[1][i - 2], dp[1][i - 3] if i >= 3 else 0) + nums[i]

        return max(dp[0][-2], dp[0][-3], dp[1][-1], dp[1][-2])