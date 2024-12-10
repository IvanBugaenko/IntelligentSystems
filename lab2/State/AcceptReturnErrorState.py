from .State import State
from ..Lexer import Lexer
from ..StateStack import StateStack


class AcceptReturnErrorState(State):
    def __init__(self, state_number: int, lexer: Lexer, stack: StateStack, next_state: int) -> None:
        self._state_number = state_number
        self._lexer = lexer
        self._stack = stack
        self._next_state = next_state

        self.is_final = True

    def next(self) -> int:
        try:
            self._lexer.check(self._state_number)
            self._lexer.accept()
            return self._stack.pop()
        except:
            raise Exception()