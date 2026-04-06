import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        time = 0
        queue = deque()
        while max_heap or queue:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt != 0:
                    queue.append([cnt, time + n])
            if queue and time == queue[0][1]:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time