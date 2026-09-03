class MinStack:

    #initialize two stacks one min one regular, linked by positions

    def __init__(self):
        self.stack_list = []
        self.stack_min_list = []
        self.current_min = float('inf')
        
    def push(self, value: int) -> None:
        self.stack_list.append(value)
        self.current_min = min(self.current_min, value)
        self.stack_min_list.append(self.current_min)
        
    def pop(self) -> None:
        self.stack_list.pop()
        self.stack_min_list.pop()
        if self.stack_min_list:
            self.current_min = self.stack_min_list[-1]
        else:
            self.current_min = float('inf')

    def top(self) -> int:
        return self.stack_list[-1]
        
    def getMin(self) -> int:
        return self.current_min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()