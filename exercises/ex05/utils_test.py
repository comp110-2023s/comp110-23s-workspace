"""untit test for untils"""

__author__ = "730575328"

from exercises.ex05.utils import only_evens, sub, concat

#unit test for the only_evans function
def test_onlyevens() -> None:
    test_list: list[int] = ([6, 4, 2])
    assert only_evens(test_list) == [6,4,2]

def test_onlyodds() -> None:
    test_list: list[int] = ([1, 5, 3])
    assert only_evens(test_list) == []

def test_empty() -> None:
    test_list: list[int] = ([])
    assert only_evens(test_list) == []