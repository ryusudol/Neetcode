import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_stones = [-stone for stone in stones]
        heapq.heapify(max_stones)
        while len(max_stones) > 1:
            s1, s2 = -heapq.heappop(max_stones), -heapq.heappop(max_stones)
            if s1 != s2:
                heapq.heappush(max_stones, -abs(s1 - s2))
        return -max_stones[0] if max_stones else 0