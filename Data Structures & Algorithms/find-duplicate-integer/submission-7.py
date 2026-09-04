class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            nums[abs(n)] *= -1
            if nums[abs(n)] > 0: return abs(n)