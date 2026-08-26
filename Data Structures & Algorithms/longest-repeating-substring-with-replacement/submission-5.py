class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alp = [0] * 26
        max_cnt, max_len, L = 0, 0, 0

        for R, c in enumerate(s):
            c_idx = ord(c) - 65
            alp[c_idx] += 1
            max_cnt = max(max_cnt, alp[c_idx])
            if (R - L + 1) - max_cnt > k:
                alp[ord(s[L]) - 65] -= 1
                L += 1
            max_len = max(max_len, R - L + 1)

        return max_len