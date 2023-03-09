"""untit test for untils!"""

__author__ = "730575328"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_use() -> None:
    """Use case test only_evens."""
    test_list: list[int] = [6, 4, 2, 5]
    assert only_evens(test_list) == [6, 4, 2]


def test_only_odds_edge2() -> None:
    """Had no even numbers at all."""
    test_list: list[int] = [1, 5, 3]
    assert only_evens(test_list) == []


def test_empty_edge2() -> None:
    """No list given."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_concat_edge() -> None:
    """No list two!"""
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = []
    assert concat(list_one, list_two) == [1, 2, 3]


def test_concat_use() -> None:
    """Use case test for concat function."""
    list_one: list[int] = ([1, 2, 3])
    list_two: list[int] = ([4, 5, 6])
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_edge2() -> None:
    """No list one."""
    list_one: list[int] = ([])
    list_two: list[int] = ([2, 3, 4, 5])
    assert concat(list_one, list_two) == [2, 3, 4, 5]


def test_sub_use() -> None:
    """Use case test for sub function!"""
    list_one: list[int] = ([10, 20, 30, 40])
    start: int = 1
    end: int = 3
    assert sub(list_one, start, end) == [20, 30, 40]


def test_sub_edge() -> None:
    """Negative Start."""
    list_one: list[int] = ([10, 20, 30, 40])
    start: int = -1
    end: int = 3
    assert sub(list_one, start, end) == [10, 20, 30]


def test_sub_edge2() -> None:
    """End is larger than length!"""
    list_one: list[int] = ([10, 20, 30, 40])
    start: int = 1
    end: int = 5
    assert sub(list_one, start, end) == [20, 30, 40]