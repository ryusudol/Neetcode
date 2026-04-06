class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt, prod_except_zero = 0, 1
        for num in nums:
            if num == 0:
                zero_cnt += 1
                if zero_cnt > 1:
                    return [0] * len(nums)
            else:
                prod_except_zero *= num
        if zero_cnt == 0:
            return [prod_except_zero // num for num in nums]
        else:
            return [prod_except_zero if num == 0 else 0 for num in nums]