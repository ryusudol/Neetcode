class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.count_palindrome(s, i, i)
            res += self.count_palindrome(s, i, i + 1)

        return res
    
    def count_palindrome(self, s: str, l: int, r: int):
        res = 0
        while 0 <= l and r < len(s) and s[l] == s[r]:
            res, l, r = res + 1, l - 1, r + 1
        return res