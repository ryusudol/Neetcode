class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res, prev = 0, 0
        comb = zip(position, speed)
        for pos, sp in sorted(comb, reverse=True):
            time = (target - pos) / sp
            if prev < time:
                res += 1
                prev = time
        return res