from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.record = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.record[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        record = self.record[key]
        l, r = 0, len(record) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            if record[m][0] <= timestamp:
                res = record[m][1]
                l = m + 1
            else:
                r = m - 1

        return res