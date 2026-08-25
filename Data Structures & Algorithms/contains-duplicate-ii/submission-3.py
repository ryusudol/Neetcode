class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for idx, num in enumerate(nums):
            if len(seen) > k: seen.discard(nums[idx - k - 1])
            if num in seen: return True
            seen.add(num)
        return False