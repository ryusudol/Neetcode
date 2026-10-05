from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_freq = max(counter.values())
        num_max = sum(1 for val in counter.values() if val == max_freq)
        frame = (max_freq - 1) * (n + 1) + num_max
        return max(len(tasks), frame)