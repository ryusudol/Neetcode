import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(p[0]**2 + p[1]**2, p) for p in points]
        heapq.heapify(dist)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(dist)[1])
        return ans