class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res, stack = 0, []
        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)
        return res