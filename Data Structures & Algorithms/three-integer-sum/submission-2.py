class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, comb_set = [], set()
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    comb = (nums[i], nums[l], nums[r])
                    if comb not in comb_set:
                        comb_set.add(comb)
                        ans.append(list(comb))
                    l, r = l + 1, r - 1
        return ans