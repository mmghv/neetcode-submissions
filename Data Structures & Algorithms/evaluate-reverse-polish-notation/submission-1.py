class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                num2, num1 = int(stack.pop()), int(stack.pop())
                match t:
                    case '+': t = num1 + num2
                    case '-': t = num1 - num2
                    case '*': t = num1 * num2
                    case '/': t = num1 / num2
            stack.append(t)
        return int(stack.pop())