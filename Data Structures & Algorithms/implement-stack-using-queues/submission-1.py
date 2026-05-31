class MyStack:
    
    def __init__(self):
        self.item=[]

    def push(self, x: int) -> None:
        self.item=[x]+self.item

    def pop(self) -> int:
        return self.item.pop(0)

    def top(self) -> int:
        return self.item[0]

    def empty(self) -> bool:
        return True if not self.item else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()