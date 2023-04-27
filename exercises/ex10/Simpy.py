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
        
#     def _getitem_(self, rhs: int) -> float: 
#        return self.values[rhs]

# a = Simpy([10.0, 20.0, 30.0])
# print("Actual: ", a[0], " - Expected: 10.0")
# print("Actual: ", a[1], " - Expected: 20.0")
# print("Actual: ", a[2], " - Expected: 30.0")


