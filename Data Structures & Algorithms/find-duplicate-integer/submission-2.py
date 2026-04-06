class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for idx, n in enumerate(nums):
            target = nums[abs(n) - 1]
            if target < 0:
                    return abs(n)
            nums[abs(n) - 1] *= -1