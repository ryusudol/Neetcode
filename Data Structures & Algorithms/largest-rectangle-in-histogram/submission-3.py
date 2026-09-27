class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res, stack = 0, []

        for idx, height in enumerate(heights + [0]):
            while stack and stack[-1][1] >= height:
                i, hei = stack.pop()
                wid = idx if not stack else idx - stack[-1][0] - 1
                res = max(res, hei * wid)
            stack.append((idx, height))

        return res