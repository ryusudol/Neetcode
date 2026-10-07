from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.upper = []
        self.lower = []

    def addNum(self, num: int) -> None:
        if self.upper and num > self.upper[0]:
            heappush(self.upper, num)
        else:
            heappush(self.lower, -1 * num)
        
        if len(self.upper) - len(self.lower) > 1:
            heappush(self.lower, -1 * heappop(self.upper))
        elif len(self.lower) - len(self.upper) > 1:
            heappush(self.upper, -1 * heappop(self.lower))

    def findMedian(self) -> float:
        if (len(self.upper) + len(self.lower)) % 2 != 0:
            return float(self.upper[0] if len(self.upper) > len(self.lower) else -1 * self.lower[0])
        else:
            return (self.upper[0] + -1 * self.lower[0]) / 2
