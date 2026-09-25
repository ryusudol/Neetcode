class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()

        nums.sort()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                first_sum = nums[i] + nums[j]
                if first_sum > target - nums[j + 1] - nums[j + 2]:
                    break
                
                l, r = j + 1, len(nums) - 1
                while l < r:
                    second_sum = nums[l] + nums[r]
                    if first_sum + second_sum == target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l, r = l + 1, r - 1
                    elif first_sum + second_sum > target:
                        r -= 1
                    else:
                        l += 1
        
        return [list(el) for el in res]