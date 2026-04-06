class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeros = 1, []
        for i, n in enumerate(nums):
            if n == 0:
                zeros.append(i)
                if len(zeros) > 1:
                    return [0] * len(nums)
            else:
                prod *= n
        if len(zeros) == 1:
            ans = [0] * len(nums)
            ans[zeros[0]] = prod
            return ans
        return [prod // n for n in nums]