import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1
        
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     m = (l + r) // 2
        #     if nums[m] < target:
        #         l = m + 1
        #     elif nums[m] > target:
        #         r = m - 1
        #     else:
        #         return m
        # return -1