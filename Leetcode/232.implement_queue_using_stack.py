class MyQueue:

    def __init__(self):
        self.stack_one = []
        # self.stack_two = []

    def push(self, x: int) -> None:
        self.stack_one.append(x)
        # self.stack_two.insert(0, x)

    def pop(self) -> int:
        res = self.stack_one.pop(0)
        # res = self.stack_two.pop(0)
        return res

    def peek(self) -> int:
        return self.stack_one[0]
        
    def empty(self) -> bool:
        return len(self.stack_one) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()