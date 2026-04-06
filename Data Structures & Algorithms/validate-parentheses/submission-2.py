class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            elif (
                not stack or
                (c == ')' and stack.pop() != '(') or
                (c == '}' and stack.pop() != '{') or
                (c == ']' and stack.pop() != '[')
            ):
                return False
        return not stack