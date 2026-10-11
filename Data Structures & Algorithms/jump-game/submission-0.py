class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for cur_reach, num in enumerate(nums):
            if cur_reach > max_reach:
                return False

            max_reach = max(max_reach, cur_reach + num)
        
        return True
