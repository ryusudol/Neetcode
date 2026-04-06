class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = max_freq = res = 0
        for r, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            max_freq = max(max_freq, count[c])
            while r - l + 1 - max_freq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res