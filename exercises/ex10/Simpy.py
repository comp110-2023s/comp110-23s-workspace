"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730575328"


class Simpy:
    """My simpy class."""
    
    values: list[float]

    def __init__(self, param: list[float]) -> None:
        """Initialize my class."""
        self.values = param

    def __str__(self) -> str:
        """Return object as a string."""
        return f'Simpy({self.values})'
    
    def fill(self, float: float, int: int) -> None:
        """Return the values into the list."""
        i = 0 
        self.values = []
        while int > i: 
            self.values.append(float)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Return a new list of ranges."""
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
        else:
            while i > stop:
                empty_list.append(index)
                index += Jump
                i += Jump
            self.values = empty_list
        return None

    def sum(self) -> float:
        """Return the sum of the float."""
        final = sum(self.values)
        return final
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Return a list of the added floats."""
        new_list = []
        i = 0 

        if type(rhs) == Simpy:
            while i < len(self.values):
                new_list.append(self[i] + rhs[i])
                i += 1
            return Simpy(new_list)

        new_list = []
        i = 0

        if type(rhs) == float:
            while i < len(self.values):
                new_list.append(self[i] + rhs)
                i += 1
            return Simpy(new_list)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Return the power of the floats."""
        new_list = []
        i = 0 

        if type(rhs) == Simpy:
            while i < len(self.values):
                new_list.append(self[i] ** rhs[i])
                i += 1
            return Simpy(new_list)

        new_list = []
        i = 0

        if type(rhs) == float:
            while i < len(self.values):
                new_list.append(self[i] ** rhs)
                i += 1
            return Simpy(new_list)
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Return if they are equal."""
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
        """Return if they are greater than."""
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
    
    def __getitem__(self, input: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Return the item."""
        if type(input) == int:
            return self.values[input]
        return_list = []
        if type(input) == list:
            for index, item in enumerate(input):
                if item is True:
                    return_list.append(self.values[index])
            return Simpy(return_list)