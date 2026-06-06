class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combs = []
        key_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def backtrack(i, cur):
            if len(cur) == len(digits):
                if digits != "": combs.append(cur)
                return

            alps = key_map[digits[i]]
            for j in range(len(alps)):
                backtrack(i + 1, cur + alps[j])
        
        backtrack(0, "")

        return combs