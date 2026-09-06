from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create a list of cars and time to reach target ina  tupple
        # sort cars by position
        # if speed at current car greater than top append 
        # return len stack
        # monotonic dec


        stack = deque()
        car_times = []
        for i in range(len(position)):
            car_times.append([position[i], (target - position[i]) / speed[i]])
        sorted_cars = sorted(car_times, reverse=True)

        stack.append(sorted_cars[0])
        for i in range(len(sorted_cars)):
            if stack and sorted_cars[i][1] > stack[-1][1]:
                stack.append(sorted_cars[i])
        
        return len(stack)
