class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def helper(i):
            if i == len(nums):
                return [[]]
            perms = helper(i + 1)
            res = []
            for p in perms:
                for j in range(len(p) + 1):
                    if j > 0 and p[j - 1] == nums[i]:
                        break
                    p_copy = p.copy()
                    p_copy.insert(j, nums[i])
                    res.append(p_copy)
            return res
        
        return helper(0)
