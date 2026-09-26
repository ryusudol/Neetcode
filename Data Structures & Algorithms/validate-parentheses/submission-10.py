class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { '(': ')', '{': '}', '[': ']' }

        for c in s:
            if c in pairs:
                stack.append(pairs[c])
            elif not stack or c != stack.pop():
                return False
        
        return not stack