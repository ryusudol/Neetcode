class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        money = {}
        for idx, num in enumerate(nums):
            money[idx] = num + max(money.get(idx - 2, 0), money.get(idx - 3, 0))
        return max(money[len(nums) - 1], money[len(nums) - 2])