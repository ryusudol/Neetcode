class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = { 0: 1 }
        cnt = cur_sum = 0
        for idx, num in enumerate(nums):
            cur_sum += num
            diff = cur_sum - k
            cnt += prefix.get(diff, 0)
            prefix[cur_sum] = prefix.get(cur_sum, 0) + 1
        return cnt