class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return max(nums)

        memo = { 0: nums[0], 1: nums[1] }
        for i in range(2, n):
            memo[i] = max(memo[i - 2], memo[i - 3] if i >= 3 else 0) + nums[i]
        
        return max(memo[n - 1], memo[n - 2])