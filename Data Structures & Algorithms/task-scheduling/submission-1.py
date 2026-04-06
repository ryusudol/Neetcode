import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        queue = deque()

        time = 0
        while heap or queue:
            time += 1
            if not heap:
                time = queue[0][1]
            else:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    queue.append((cnt, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time