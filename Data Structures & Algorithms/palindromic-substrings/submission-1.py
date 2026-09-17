class Solution:
    def countSubstrings(self, s: str) -> int:
        res, cur_len = len(s), 2

        while cur_len <= len(s):
            for i in range(len(s) - cur_len + 1):
                cur_str = s[i : i + cur_len]
                res += 1 if cur_str == cur_str[::-1] else 0
            cur_len += 1

        return res