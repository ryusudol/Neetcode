class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = { 0: 1 }
        cnt = cur_sum = 0
        for idx, num in enumerate(nums):
            cur_sum += num
            diff = cur_sum - k
            cnt += memo.get(diff, 0)
            memo[cur_sum] = memo.get(cur_sum, 0) + 1
        return cnt