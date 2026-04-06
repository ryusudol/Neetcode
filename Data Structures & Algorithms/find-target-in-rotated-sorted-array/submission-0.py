class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        if nums[l] <= target <= nums[-1]:
            r = len(nums) - 1
        else:
            l = 0
            r -= 1
        while l < r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        return l if nums[l] == target else -1