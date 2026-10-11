class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jump = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            min_jump += 1
        
        return min_jump