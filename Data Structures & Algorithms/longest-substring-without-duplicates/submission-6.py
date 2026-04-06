class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = length = 0

        for r, c in enumerate(s):
            if c in seen:
                while c in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            length = max(length, r - l + 1)
        
        return length