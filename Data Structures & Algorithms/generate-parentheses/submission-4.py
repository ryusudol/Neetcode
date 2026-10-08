from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur: List[str], op: int, cl: int) -> None:
            if op == cl == n:
                res.append("".join(cur))
                return
            if op < n:
                cur.append("(")
                backtrack(cur, op + 1, cl)
                cur.pop()
            if cl < op:
                cur.append(")")
                backtrack(cur, op, cl + 1)
                cur.pop()

        backtrack([], 0, 0)

        return res
