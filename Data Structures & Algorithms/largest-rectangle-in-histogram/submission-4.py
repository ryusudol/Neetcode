class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res, stack = 0, []

        for idx, height in enumerate(heights + [0]):
            while stack and stack[-1][1] >= height:
                _, h = stack.pop()
                width = idx if not stack else idx - stack[-1][0] - 1
                res = max(res, h * width)
            stack.append((idx, height))
        
        return res
