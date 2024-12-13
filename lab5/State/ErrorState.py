import typing as t
from .State import State
from ..Lexer import Lexer
from ..Stack import Stack


class ErrorState(State):
    def __init__(self, symbol: str, i: str, state_stack: Stack, symbol_stack: Stack, lexer: Lexer) -> None:
        self._symbol = symbol
        self._i = i
        self._state_stack = state_stack
        self._symbol_stack = symbol_stack
        self._lexer = lexer
        
    def next(self) -> t.Tuple[str, str]:
        raise Exception()