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

    def arange(self, start: float, stop: float, step: float = 1.0) -> list[float]:
        i: int = start
        index: int = start
        Jump: int = step
        empty_list = list[float]
        while i < stop:
            index += Jump
            empty_list.append(index)
            i += 1.0
        
        return self.values
    

positive = Simpy([])
positive.arange(1.0, 5.0)
print("Actual: ", positive, " - Expected: Simpy([1.0, 2.0, 3.0, 4.0])")