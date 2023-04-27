"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730575328"


class Simpy:
    """My simpy class."""
    
    values: list[float]

    def __init__(self, param: list[float]) -> None:
        """Initializes my class."""
        self.values = param

    def __str__(self) -> str:
        """Returns object as a string."""
        return f'Simpy({self.values})'
    
    def fill(self, float: float, int: int) -> None:
        """Appends values into the list."""
        i = 0 
        self.values = []
        while int > i: 
            self.values.append(float)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> list[float]:
        """Works as a range function."""
        i: int = start
        index: int = start
        Jump: float = step
        empty_list = []
        if start >= 0:
            while i < stop:
                empty_list.append(index)
                index += Jump
                i += Jump
            self.values = empty_list
            return self.values
        else:
            while i > stop:
                empty_list.append(index)
                index += Jump
                i += Jump
            self.values = empty_list
            return self.values


    def sum(self) -> float:
        """Sums floats."""
        final = sum(self.values)
        return final
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds the floats."""
        new_list: list[Union[Simpy, float]] = []
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
        """Powers the floats."""
        new_list: list[Union[Simpy, float]] = []
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
        """Returns if they are equal."""
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
        """Returns of they are greater than."""
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
           