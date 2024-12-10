import typing as t


class Lexer:
    def __init__(self, guiding_symbols: t.Dict[int, t.List[str]]) -> None:
        self.token_sequence = None
        self.guiding_symbols = guiding_symbols

    def get_current_token(self) -> str:
        return self.token_sequence[0]
    
    def set_token_sequence(self, token_sequence: str) -> None:
        self.token_sequence = token_sequence
    
    def check(self, current_state_number: int) -> None:
        assert self.get_current_token() in self.guiding_symbols[current_state_number]

    def accept(self) -> None:
        self.token_sequence = self.token_sequence[1:]
