from heapq import heapify, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [(x ** 2 + y ** 2, x, y) for x, y in points]
        heapify(dists)
        res = []
        for i in range(k):
            _, x, y = heappop(dists)
            res.append([x, y])
        return res