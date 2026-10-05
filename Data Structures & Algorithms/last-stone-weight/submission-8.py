from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)

        while len(stones) > 1:
            st1, st2 = -heappop(stones), -heappop(stones)
            remain = st1 - st2
            if remain:
                heappush(stones, -remain)

        return -stones[0] if stones else 0