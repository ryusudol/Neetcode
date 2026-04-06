class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len, l = 0, 0
        alp = set()
        for r, c in enumerate(s):
            while c in alp:
                alp.remove(s[l])
                l += 1
            alp.add(c)
            longest_len = max(longest_len, r - l + 1)
        return longest_len