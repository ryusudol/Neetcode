class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        memo = {0: nums[0], 1: max(nums[0], nums[1]), 2: nums[0] + nums[2]}
        for i in range(3, len(nums)):
            memo[i] = max(memo[i - 2], memo[i - 3]) + nums[i]
        return max(memo[len(nums) - 1], memo[len(nums) - 2])