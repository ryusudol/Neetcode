class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        while l <= r:
            m = (l + r) // 2
            time = sum(p // m + (1 if p % m else 0) for p in piles)
            if time <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        
        return k