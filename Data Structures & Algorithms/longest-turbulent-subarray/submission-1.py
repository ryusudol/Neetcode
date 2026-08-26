class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, max_len = 0, 1
        prev_state, cur_state = 0, 0

        for R in range(1, len(arr)):
            prev, cur = arr[R - 1], arr[R]
            cur_state = 1 if prev < cur else 2 if prev == cur else 3
            if cur_state == 2:
                L = R
            elif cur_state == prev_state:
                L = R - 1
            prev_state = cur_state
            max_len = max(max_len, R - L + 1)
        
        return max_len