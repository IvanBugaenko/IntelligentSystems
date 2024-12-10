from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def next(self) -> int:
        pass
