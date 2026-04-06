class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(stack)
            if t not in "+-*/":
                stack.append(int(t))
            else:
                a, b = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(b / a))
        return stack[-1]