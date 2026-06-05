class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, comb, total):
            if i >= len(nums) or total > target: return
            if total == target:
                res.append(comb.copy())
                return

            comb.append(nums[i])
            backtrack(i, comb, total + nums[i])
            comb.pop()
            backtrack(i + 1, comb, total)

        backtrack(0, [], 0)

        return res