from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_count][:k]