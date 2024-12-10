from .State import State
from ..Lexer import Lexer
from ..StateStack import StateStack


class ErrorStackState(State):
    def __init__(self, state_number: int, lexer: Lexer, stack: StateStack, next_state: int) -> None:
        self._state_number = state_number
        self._lexer = lexer
        self._stack = stack
        self._next_state = next_state

        self.is_final = False

    def next(self) -> int:
        try:
            self._lexer.check(self._state_number)
            self._stack.push(self._state_number + 1)
            return self._next_state
        except:
            raise Exception()
