class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def helper(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            helper(i + 1, cur)
            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, cur)
        
        helper(0, [])
        return res