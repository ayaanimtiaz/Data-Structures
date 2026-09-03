from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # stack: 4, 13, 5
        # create total var
        # if current element is an operator
        # pop last two in stack, use operator
        # account for edge cases
        # add each operation to the total variable

        stack_var = deque()
        operators = {"+", "-", "*", "/"}


        for i in range(len(tokens)):
            if tokens[i] in operators:
                new_element = stack_var.pop()
                previous_element = stack_var.pop()
                #substitute
                if tokens[i] == '+':
                    stack_var.append(previous_element + new_element)
                elif tokens[i] == '*':
                    stack_var.append(previous_element * new_element)
                elif tokens[i] == '/':
                    stack_var.append(int(previous_element / new_element))
                elif tokens[i] == '-':
                    stack_var.append(previous_element - new_element)

            else:
                stack_var.append(int(tokens[i]))
        return stack_var[-1]