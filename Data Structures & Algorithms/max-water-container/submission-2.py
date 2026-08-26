class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        L, R = 0, len(heights) - 1
        while L < R:
            lh, rh = heights[L], heights[R]
            max_water = max(max_water, (R - L) * min(lh, rh))
            if lh <= rh: L += 1
            else: R -= 1
        return max_water