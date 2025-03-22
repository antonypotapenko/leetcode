class MyQueue:

    def __init__(self):
        self.begin_stack = []
        self.end_stack = []

    def push(self, x: int) -> None:
        self.end_stack.append(x)
        self.begin_stack = self.end_stack[::-1]

    def pop(self) -> int:
        value = self.begin_stack.pop()
        self.end_stack = self.begin_stack[::-1]
        return value

    def peek(self) -> int:
        return self.begin_stack[-1]


    def empty(self) -> bool:
        if self.begin_stack and self.end_stack:
            return False
        return True
