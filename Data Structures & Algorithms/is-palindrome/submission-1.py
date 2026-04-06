class Solution:
    def isPalindrome(self, s: str) -> bool:
        a, b = 0, len(s) - 1
        s = s.lower()
        while a <= b:
            if not s[a].isalpha() and not s[a].isdigit():
                a += 1
                continue
            elif not s[b].isalpha() and not s[b].isdigit():
                b -= 1
                continue
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True