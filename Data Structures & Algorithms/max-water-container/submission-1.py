class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = water = 0
        r = len(heights) - 1
        while l < r:
            water = max(water, (r - l) * min(heights[l], heights[r]))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return water