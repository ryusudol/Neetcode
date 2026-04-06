class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_length = 0
        nums = set(nums)
        for n in nums:
            if n - 1 not in nums:
                cur_len = 0
                while n in nums:
                    cur_len += 1
                    n += 1
                longest_length = max(longest_length, cur_len)
        return longest_length