class StateStack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> int:
        return self.stack.pop(-1)
    
    def is_empty(self) -> bool:
        return len(self.stack) == 0
