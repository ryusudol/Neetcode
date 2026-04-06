class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights) - 1
        while l < r:
            if heights[l] <= heights[r]:
                water = (r - l) * heights[l]
                l += 1
            else:
                water = (r - l) * heights[r]
                r -= 1
            max_water = max(max_water, water)
        return max_water