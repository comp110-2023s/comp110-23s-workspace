"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730575328"


class Simpy:
    
    values: list[float]

    def __init__(self, param: list[float]) -> None:
        self.values = param

    def __str__(self) -> str:
        return f'simpy({self.values})'
    
    def fill(self, float: float, int: int) -> None:
        i = 0 
        while int > i: 
            self.values.append(float)
            i += 1

    def arange(self, start: float, stop: float, step: float):
        