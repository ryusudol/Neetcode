class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        L, cur_sum = 0, 0

        for R, num in enumerate(nums):
            cur_sum += num
            while cur_sum >= target:
                res = min(res, R - L + 1)
                cur_sum -= nums[L]
                L += 1
        
        return res if res != float('inf') else 0