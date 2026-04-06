class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        for i in range(len(nums)):
            left_sum = prefix[i - 1] if i > 0 else 0
            right_sum = prefix[-1] - prefix[i]
            if left_sum == right_sum:
                return i
        return -1