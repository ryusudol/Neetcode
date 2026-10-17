class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def check(start: int, end: int) -> None:
            nonlocal res
            while 0 <= start and end < len(s) and s[start] == s[end]:
                res = s[start:end + 1] if len(res) < end - start + 1 else res
                start, end = start - 1, end + 1
        
        for i in range(len(s)):
            check(i, i)
            check(i, i + 1)
        
        return res