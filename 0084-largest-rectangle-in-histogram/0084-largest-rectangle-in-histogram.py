from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # do a while pop when we encounter something less than, make sure the starting index is the smae as the last one popped.

        stack = deque()

        curr = 0

        for i in range(len(heights)):
            if stack and heights[i] < stack[-1][0]:
                saving_index = i 
                while stack and heights[i] < stack[-1][0]:
                    saving_index = stack[-1][1]
                    curr = max(curr, stack[-1][0] * (i - stack[-1][1]))
                    stack.pop()
                stack.append([heights[i], saving_index])
            else:
                stack.append([heights[i], i])
        
        while stack:
            curr = max(curr, stack[-1][0] * (len(heights) - stack[-1][1]))
            stack.pop()
        
        return curr

            




