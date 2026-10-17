class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        def helper(start: int, end: int) -> int:
            r1 = r2 = 0
            for i in range(start, end + 1):
                r1, r2 = r2, max(r1 + nums[i], r2)
            return r2
        
        return max(helper(0, n - 2), helper(1, n - 1))