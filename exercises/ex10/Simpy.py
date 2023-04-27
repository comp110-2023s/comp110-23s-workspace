"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730575328"


class Simpy:
    
    values: list[float]

    def __init__(self, param: list[float]) -> None:
        self.values = param

    def __str__(self) -> str:
        return f'Simpy({self.values})'
    
    def fill(self, float: float, int: int) -> None:
        i = 0 
        self.values = []
        while int > i: 
            self.values.append(float)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> list[float]:
        i: int = start
        index: int = start
        Jump: int = step
        empty_list = []
        while i < stop:
            empty_list.append(index)
            index += Jump
            i += 1.0
        self.values = empty_list
        return self.values

    def sum(self) -> float:
        final = sum(self.values)
        return final
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        new_list: list[Union[Simpy,float]] = []
        i = 0 

        if type(rhs) == Simpy:
            while i < len(self.values):
                new_list.append(self.values[i] + rhs.values[i])
                i += 1
            return f"Simpy({new_list})"

        new_list = []
        i = 0

        if type(rhs) == float:
            while i < len(self.values):
                new_list.append(self.values[i] + rhs)
                i += 1
            return f"Simpy({new_list})"

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        new_list: list[Union[Simpy,float]] = []
        i = 0 

        if type(rhs) == Simpy:
            while i < len(self.values):
                new_list.append(self.values[i] ** rhs.values[i])
                i += 1
            return f"Simpy({new_list})"

        new_list = []
        i = 0

        if type(rhs) == float:
            while i < len(self.values):
                new_list.append(self.values[i] ** rhs)
                i += 1
            return f"Simpy({new_list})"
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        new_list: list[Union[float, Simpy]] = []
        i = 0 

        if type(rhs) == Simpy:
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1
            return new_list
        
        if type(rhs) == float:
            while i < len(self.values):
                if self.values[i] == rhs:
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1
            return new_list
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        new_list: list[Union[float, Simpy]] = []
        i = 0 

        if type(rhs) == Simpy:
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1
            return new_list
        
        if type(rhs) == float:
            while i < len(self.values):
                if self.values[i] > rhs:
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1
            return new_list 
        
twos = Simpy([])
twos.fill(2.0, 3)
print("Actual: ", twos, " - Expected: Simpy([2.0, 2.0, 2.0])") 
twos.fill(2.0, 5)
print("Actual: ", twos, " - Expected: Simpy([2.0, 2.0, 2.0, 2.0, 2.0])")

mixed = Simpy([])
mixed.fill(3.0, 3)
print("Actual: ", mixed, " - Expected: Simpy([3.0, 3.0, 3.0])")
mixed.fill(2.0, 2)
print("Actual: ", mixed, " - Expected: Simpy([2.0, 2.0])")