from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # each operation in the stack builds on top of itself
        stack = deque()
        operations = {"+", "-", "/", "*"}
        for i in range(len(tokens)):
            if tokens[i] in operations:
                first_element = int(stack.pop())
                second_element = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(second_element + first_element)
                if tokens[i] == '-':
                    stack.append(second_element - first_element)
                if tokens[i] == '/':
                    stack.append(int(second_element / first_element))
                if tokens[i] == '*':
                    stack.append(second_element * first_element)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]