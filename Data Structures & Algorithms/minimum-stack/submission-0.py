class StackNode:
    def __init__(self, value=None, prev=None, min_val=float('inf')):
        self.value = value
        self.prev = prev
        self.min_val = min_val

class MinStack:

    def __init__(self):
        self.stack = StackNode()
        

    def push(self, val: int) -> None:
        cur_node = StackNode(val, self.stack, min(self.stack.min_val, val))
        self.stack = cur_node

    def pop(self) -> None:
        self.stack = self.stack.prev

    def top(self) -> int:
        return self.stack.value

    def getMin(self) -> int:
        return self.stack.min_val
        
