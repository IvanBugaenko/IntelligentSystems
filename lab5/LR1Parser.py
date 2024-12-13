import pandas as pd
import typing as t
from .State.State import State
from .Lexer import Lexer
from .Stack import Stack
from .State import State, ErrorState, STerminalState, SNonTerminalState, RState


class LR1Parser:
    def __init__(self, table: pd.DataFrame, rules_meta: t.Dict[str, t.Dict[str, int | str]], terminal_symbols: t.List[str]) -> None:
        self._state_stack = Stack()
        self._symbol_stack = Stack()
        self._lexer = Lexer(rules_meta)
        self._symbol_table: t.Dict[t.Tuple[str, str]: State] = self.__get_symbol_table(table.to_dict(), terminal_symbols)
        
    def __get_symbol_table(self, symbol_table_str: t.Dict[str, t.Dict[int, str]], terminal_symbols: t.List[str]) -> t.Dict[t.Tuple[str, str], State]:
        res = {}
        action_states = {
            ('s', True): STerminalState,
            ('s', False): SNonTerminalState,
            ('r', True): RState,
            ('r', False): RState,
            'e': ErrorState
        }
        
        for symbol in symbol_table_str.keys():
            for state_id in symbol_table_str[symbol].keys():
                value = symbol_table_str[symbol][state_id]
                try:
                    s_type = value[0]
                    i = str(value[1:])
                    key = (s_type, symbol in terminal_symbols)
                except:
                    i = None
                    key = 'e'
                    
                state = action_states[key](
                    symbol, i, self._state_stack, self._symbol_stack, self._lexer
                )
            
                res[(symbol, str(state_id))] = state
                
        return res
                
    def analyze(self, word: str, start_state_id: str = '0', sos_symbol: str = 'S', eof_symbol: str = 'eof') -> bool:
        self._state_stack.stack = [start_state_id]

        token_sequence = word.split()
        token_sequence.append(eof_symbol)
        self._lexer.set_token_sequence(token_sequence)
        
        start_symbol = self._lexer.get_current_token()
        
        while not (
            start_symbol == sos_symbol and 
            self._symbol_stack.is_empty() and 
            self._state_stack.watch_head() == start_state_id and
            self._state_stack.len() == 1
        ):
            try:
                start_symbol, start_state_id = self._symbol_table[(start_symbol, start_state_id)].next()
            except:
                return False
        return True
