import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            crash = -abs(s1 - s2)
            if crash:
                heapq.heappush(stones, crash)
        return -stones[0] if stones else 0