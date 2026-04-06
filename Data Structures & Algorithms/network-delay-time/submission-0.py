import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((t, v))
        ans, costs = 0, {}
        pq = [(0, k)]
        while pq:
            cur_cost, cur_v = heapq.heappop(pq)
            if cur_v not in costs:
                costs[cur_v] = cur_cost
                ans = max(ans, cur_cost)
                for cost, neighbor in graph[cur_v]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, neighbor))
        return ans if len(costs) == n else -1