class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        def backtrack(i, cur):
            if len(cur) == k:
                combs.append(cur.copy())
                return
            if i > n: return

            for val in range(i, n + 1):
                cur.append(val)
                backtrack(val + 1, cur)
                cur.pop()
        
        backtrack(1, [])

        return combs