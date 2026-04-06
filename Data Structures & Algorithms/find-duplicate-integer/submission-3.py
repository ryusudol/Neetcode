class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for idx, n in enumerate(nums):
            idx = abs(n) - 1
            if nums[idx] < 0:
                    return abs(n)
            nums[idx] *= -1