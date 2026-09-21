class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt, mult, res = 0, 1, []
        for num in nums:
            if num == 0:
                zero_cnt += 1
                if zero_cnt > 1:
                    return [0] * len(nums)
            else:
                mult *= num
        
        return [mult // num for num in nums] if zero_cnt == 0 else [0 if num != 0 else mult for num in nums]