class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.max_size = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if self.max_size < len(self.cache.keys()):
            del self.cache[next(iter(self.cache))]