class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        perms = [[]]

        for n in nums:
            new_perms = []

            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)

                    if i < len(p) and n == p[i]:
                        break

            perms = new_perms
        return perms