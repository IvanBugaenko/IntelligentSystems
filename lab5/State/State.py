from __future__ import annotations
from abc import ABC, abstractmethod
import typing as t


class State(ABC):
    @abstractmethod
    def next(self) -> t.Tuple[str, str]:
        pass
