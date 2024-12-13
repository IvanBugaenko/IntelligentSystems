import typing as t


class Lexer:
    def __init__(self, rules_meta: t.Dict[str, t.Dict[str, int | str]]) -> None:
        self._token_sequence: list = None
        self.rules_meta = rules_meta
        
    def set_token_sequence(self, token_sequence: t.List[str]) -> None:
        self._token_sequence = token_sequence

    def get_current_token(self) -> str:
        return self._token_sequence[0]
        
    def accept(self) -> None:
        self._token_sequence = self._token_sequence[1:]
