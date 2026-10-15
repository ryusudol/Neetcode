from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = [False] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node: int):
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        res = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                res += 1
        
        return res
