import typing as t


class Stack:
    def __init__(self) -> None:
        self.stack = []
        
    def push(self, value: t.Any) -> None:
        self.stack.append(value)
        
    def pop_n(self, n: int = 1) -> t.List[t.Any]:
        return [self.stack.pop(-1) for _ in range(n)]
    
    def watch_head(self) -> t.Any:
        return self.stack[-1]
    
    def len(self) -> int:
        return len(self.stack)
    
    def is_empty(self) -> bool:
        return self.len() == 0
