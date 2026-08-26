class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        l_max, r_max = height[L], height[R]
        trapped_water = 0

        while L < R:
            if height[L] <= height[R]:
                l_max = max(l_max, height[L])
                trapped_water += l_max - height[L]
                L += 1
            else:
                r_max = max(r_max, height[R])
                trapped_water += r_max - height[R]
                R -= 1
        
        return trapped_water