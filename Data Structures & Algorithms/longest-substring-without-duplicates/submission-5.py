class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len, l = 0, 0
        alp = {}
        for r, c in enumerate(s):
            if c in alp:
                l = max(alp[c] + 1, l)
            alp[c] = r
            longest_len = max(longest_len, r - l + 1)
        return longest_len