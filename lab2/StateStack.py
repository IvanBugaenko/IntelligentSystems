class StateStack:
    def __init__(self) -> None:
        self._stack = []

    def push(self, value: int) -> None:
        self._stack.append(value)

    def pop(self) -> int:
        return self._stack.pop(-1)
    
    def is_empty(self) -> bool:
        return len(self._stack) == 0
