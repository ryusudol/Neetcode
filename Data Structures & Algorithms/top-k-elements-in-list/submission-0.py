class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = defaultdict(int)
        for num in nums:
            memo[num] += 1
        return [key for key, _ in sorted(memo.items(), key=lambda x: x[1], reverse=True)[:k]]