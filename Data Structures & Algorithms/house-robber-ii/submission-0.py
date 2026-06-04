class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 3: return max(nums)

        # case 1) exclude
        dp = { 0: 0, 1: nums[1], 2: max(nums[1:3]) }
        for i in range(3, n):
            dp[i] = max(dp[i - 1], max(dp[i - 2], dp[i - 3]) + nums[i])

        res = dp[n - 1]

        # case 2) include
        dp = { 0: nums[0], 1: nums[0], 2: nums[0] + nums[2] }
        for i in range(3, n - 1):
            dp[i] = max(dp[i - 1], max(dp[i - 2], dp[i - 3]) + nums[i])
        
        res = max(res, dp[n - 2])

        return res