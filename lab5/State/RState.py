import typing as t
from .State import State
from ..Lexer import Lexer
from ..Stack import Stack


class RState(State):
    def __init__(self, symbol: str, i: str, state_stack: Stack, symbol_stack: Stack, lexer: Lexer) -> None:
        self._symbol = symbol
        self._i = i
        self._state_stack = state_stack
        self._symbol_stack = symbol_stack
        self._lexer = lexer
        
    def next(self) -> t.Tuple[str, str]:
        n = self._lexer.rules_meta[self._i]['right_n']
        _ = self._state_stack.pop_n(n)
        _ = self._symbol_stack.pop_n(n)
        
        return self._lexer.rules_meta[self._i]['left_symbol'], self._state_stack.watch_head()
    
    def __repr__(self):
        return f'r{self._i}'
