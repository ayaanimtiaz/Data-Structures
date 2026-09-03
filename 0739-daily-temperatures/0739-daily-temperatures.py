from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # make a stack with a temp and an index
        # check -2  of stack


        stack_temp = deque()
        result = [0] * len(temperatures)
        curr_elm = 0

        # we hvae to loop thru
        # for loop with enumerate
        # while the stack does exist and the current temperature is higher than the top of the stack
        # pop and place to result
        

        for index, current_temp in enumerate(temperatures):
            while stack_temp and current_temp > stack_temp[-1][0]:
                result[stack_temp[-1][1]] = index - stack_temp[-1][1]
                stack_temp.pop()
            stack_temp.append([current_temp, index])
        return result