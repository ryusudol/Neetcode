class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alph = set()
        res, L = 0, 0

        for R, c in enumerate(s):
            while c in alph:
                alph.discard(s[L])
                L += 1
            alph.add(c)
            res = max(res, R - L + 1)
        
        return res