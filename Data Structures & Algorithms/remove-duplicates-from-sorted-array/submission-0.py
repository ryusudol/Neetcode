class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        while p < len(nums):
            if nums[p - 1] == nums[p]:
                del nums[p]
                continue
            p += 1
        return len(nums)