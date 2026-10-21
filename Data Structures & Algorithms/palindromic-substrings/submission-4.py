class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def check(start: int, end: int) -> None:
            nonlocal res

            while 0 <= start and end < n:
                if s[start] == s[end]:
                    res += 1
                    start, end = start - 1, end + 1
                else:
                    return

        for i in range(n):
            check(i, i)
            check(i, i + 1)

        return res
