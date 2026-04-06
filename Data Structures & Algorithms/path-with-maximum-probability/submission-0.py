import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for idx, edge in enumerate(edges):
            graph[edge[0]].append((succProb[idx], edge[1]))
            graph[edge[1]].append((succProb[idx], edge[0]))
        
        costs = {}
        pq = [(-1, start_node)]
        while pq:
            cur_prob, cur_v = heapq.heappop(pq)
            if cur_v not in costs:
                costs[cur_v] = -cur_prob
                for prob, next_v in graph[cur_v]:
                    next_prob = cur_prob * prob
                    heapq.heappush(pq, (next_prob, next_v))
        
        return costs[end_node] if end_node in costs else 0