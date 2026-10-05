from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        for i in range(k - 1):
            heappop(nums)
        return -nums[0]