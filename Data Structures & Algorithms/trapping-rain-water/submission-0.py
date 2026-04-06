class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        while l < r:
            min_lr = min(max_l, max_r)
            if max_l <= max_r:
                water = min_lr - height[l]
                l += 1
                max_l = max(max_l, height[l])
            else:
                water = min_lr - height[r]
                r -= 1
                max_r = max(max_r, height[r])
            if water > 0:
                total_water += water
        return total_water