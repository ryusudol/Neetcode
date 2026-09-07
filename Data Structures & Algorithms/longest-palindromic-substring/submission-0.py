class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''

        def check(left: int, right: int):
            nonlocal res
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res = s[left:right + 1] if len(res) <= right - left + 1 else res
                left, right = left - 1, right + 1

        for i in range(len(s)):
            check(i, i)
            check(i, i + 1)

        return res