class MinStack:

    def __init__(self):
        self.stack = []
        self.minList = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minList) == 0 or val < self.minList[-1][1]:
            self.minList.append((len(self.stack)-1, val))
        

    def pop(self) -> None:
        self.stack.pop()
        if len(self.minList) and self.minList[-1][0] == len(self.stack):
            self.minList.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minList[-1][1]
