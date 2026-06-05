class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(i, cur_subset):
            if i >= len(nums):
                subsets.append(cur_subset.copy())
                return
            
            cur_subset.append(nums[i])
            backtrack(i + 1, cur_subset)
            cur_subset.pop()
            backtrack(i + 1, cur_subset)
        
        backtrack(0, [])

        return subsets