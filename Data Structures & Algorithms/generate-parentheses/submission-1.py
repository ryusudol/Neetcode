from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur: List[str], op: int, cl: int) -> None:
            if op == cl:
                if op < n:
                    cur.append("(")
                    backtrack(cur, op + 1, cl)
                    cur.pop()
                else:
                    res.append("".join(cur))
                    return
            elif op > cl:
                if op < n:
                    cur.append("(")
                    backtrack(cur, op + 1, cl)
                    cur.pop()

                    cur.append(")")
                    backtrack(cur, op, cl + 1)
                    cur.pop()
                elif op == n:
                    cur.append(")")
                    backtrack(cur, op, cl + 1)
                    cur.pop()

        backtrack([], 0, 0)

        return res
