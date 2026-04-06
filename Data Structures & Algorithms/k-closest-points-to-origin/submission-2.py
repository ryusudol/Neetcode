import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ### Max Heap ### -> O(n + nlogk) Time, O(k) Space
        # max_heap = []
        # for x, y in points:
        #     dist = -(x ** 2 + y ** 2)
        #     heapq.heappush(max_heap, (dist, x, y))
        #     if len(max_heap) > k:
        #         heapq.heappop(max_heap)
        # ans = []
        # while max_heap:
        #     dist, x, y = heapq.heappop(max_heap)
        #     ans.append([x, y])
        # return ans

        ### Min Heap ### -> O(n + klogn) Time, O(n) Space
        dist = [(p[0]**2 + p[1]**2, p) for p in points]
        heapq.heapify(dist)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(dist)[1])
        return ans