class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)

        rob = {0: nums[0], 1: max(nums[:2])}
        for i in range(2, len(nums)):
            rob[i] = max(rob[i - 2], rob[i - 3] if i > 2 else 0) + nums[i]
        print(rob)
        return max(rob[len(nums) - 1], rob[len(nums) - 2])