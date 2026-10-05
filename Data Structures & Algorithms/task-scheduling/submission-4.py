from collections import Counter, deque
from heapq import heapify, heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [(-cnt, task) for task, cnt in counter.items()]
        heapify(heap)

        queue = deque()  # (available_time, (cnt, task))
        elapsed_time = 0

        while heap or queue:
            elapsed_time += 1

            if queue and queue[0][0] == elapsed_time:
                _, (cnt, task) = queue.popleft()
                heappush(heap, (-cnt, task))

            if heap:
                cnt, task = heappop(heap)
                if -cnt - 1 > 0:
                    queue.append((elapsed_time + n + 1, (-cnt - 1, task)))
        
        return elapsed_time
