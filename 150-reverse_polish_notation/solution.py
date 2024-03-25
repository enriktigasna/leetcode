# Beats 82.63% in memory

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        stack = []
        while tokens:
            stack.append(tokens.pop(0))
            if stack[-1] in operators:
                operator = stack.pop()
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                if (operator == "+"):
                    stack.append(operand1 + operand2)
                if (operator == "-"):
                    stack.append(operand1 - operand2)
                if (operator == "*"):
                    stack.append(operand1 * operand2)
                if (operator == "/"):
                    if operand1 / operand2 < 0:
                        stack.append(ceil(operand1 / operand2))
                    else:
                        stack.append(floor(operand1 / operand2))
        return(int(stack[0]))