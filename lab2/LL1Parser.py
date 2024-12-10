from .State.State import State
from .State.AcceptErrorState import AcceptErrorState
from .State.AcceptReturnErrorState import AcceptReturnErrorState
from .State.ErrorStackState import ErrorStackState
from .State.ZeroState import ZeroState
from .State.ErrorState import ErrorState
from .State.ReturnErrorState import ReturnErrorState
from .Lexer import Lexer
from .StateStack import StateStack
import pandas as pd
import typing as t


class LL1Parser:
    def __init__(self, rules: pd.DataFrame) -> None:
        self._lexer = Lexer(self.__get_guiding_symbols(rules))
        self._stack = StateStack()
        self._state_dict = self.__get_state_dict(rules, self._lexer, self._stack)

    def __get_guiding_symbols(self, rules: pd.DataFrame) -> t.Dict[int, t.List[str]]:
        return {
            row['State']: row['M'].split() for _, row in rules.iterrows()
        }

    def __get_state_dict(self, rules: pd.DataFrame, lexer: Lexer, stack: StateStack) -> t.Dict[int, State]:
        row2class = {
            (0, 0, 0, 0): ZeroState,
            (0, 0, 1, 0): ErrorState,
            (0, 0, 1, 1): ErrorStackState,
            (0, 1, 1, 0): ReturnErrorState,
            (1, 0, 1, 0): AcceptErrorState,
            (1, 1, 1, 0): AcceptReturnErrorState,
        }
        return {
            row['State']: row2class[tuple(row[['Accept', 'Return', 'Error', 'Stack']])](
                row['State'], 
                lexer, 
                stack, 
                row['NextState']
            ) for _, row in rules.iterrows()
        }
    
    def analyze(self, word: str, start_state_id: int = 100, eof_symbol: str = 'eof') -> bool:
        token_sequence = word.split()
        token_sequence.append(eof_symbol)
        self._lexer.set_token_sequence(token_sequence)

        while not (self._stack.is_empty() and self._lexer.get_current_token() == eof_symbol and self._state_dict[start_state_id].is_final):
            try:
                start_state_id = self._state_dict[start_state_id].next()
            except:
                return False
        return True
