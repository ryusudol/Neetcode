class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        res = []
        key_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }

        def helper(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for key in key_map[digits[i]]:
                cur += key
                helper(i + 1, cur)
                cur = cur[:-1]

        helper(0, "")
        return res