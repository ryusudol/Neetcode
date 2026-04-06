from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, target_list = "", self.store.get(key, [])
        l, r = 0, len(target_list) - 1
        while l <= r:
            m = (l + r) // 2
            if target_list[m][0] <= timestamp:
                res = target_list[m][1]
                l = m + 1
            else:
                r = m - 1
        return res