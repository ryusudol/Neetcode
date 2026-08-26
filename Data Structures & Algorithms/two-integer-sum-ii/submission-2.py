class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R:
            cur_sum = numbers[L] + numbers[R]
            if target < cur_sum: R -= 1
            elif cur_sum < target: L += 1
            else: return [L + 1, R + 1]