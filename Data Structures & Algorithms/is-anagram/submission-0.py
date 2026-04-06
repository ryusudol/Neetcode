class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen1, seen2 = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            seen1[s[i]] += 1
            seen2[t[i]] += 1
        return seen1 == seen2