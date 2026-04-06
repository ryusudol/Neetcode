import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x, y in points:
            d = x**2 + y**2
            heapq.heappush(dist, (-d, x, y))
            if len(dist) > k:
                heapq.heappop(dist)
        return [[d[1], d[2]] for d in dist]