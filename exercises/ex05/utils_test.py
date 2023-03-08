"""Unit Tests for EX05."""

__author__ = "730556365"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_all_odds() -> None:
    """Tests the only_evens function when all numbers in the list are odd."""
    test_list: list[int] = [3, 9, 19]
    assert only_evens(test_list) == []  


def test_only_evens_mixed() -> None:
    """Tests the only_evens function when there are both even and odd numbers in the list."""
    test_list: list[int] = [6, 9, 14]
    assert only_evens(test_list) == [6, 14]  


def test_only_evens_empty() -> None:
    """Tests the only_evens function when the list is empty."""
    assert only_evens([]) == []


def test_concat_single_values() -> None:
    """Tests the concat function when each list only has one value."""
    test_one: list[int] = [10]
    test_two: list[int] = [20]
    assert concat(test_one, test_two) == [10, 20]


def test_concat_mult_values() -> None:
    """Tests the concat function when each list has multiple values."""
    test_one: list[int] = [3, 2, 1, 0]
    test_two: list[int] = [1, 2, 3]
    assert concat(test_one, test_two) == [3, 2, 1, 0, 1, 2, 3]


def test_concat_one_list_empty() -> None:
    """Tests the concat function when one of the lists is empty."""
    test_one: list[int] = list()
    test_two: list[int] = [100]
    assert concat(test_one, test_two) == [100]


def test_sub_middle() -> None:
    """Tests the sub function's ability to create a list from values in the middle of the original list."""
    test_list: list[int] = [5, 8, 2, 9, 11, 1, 16]
    start: int = 2
    end: int = 5
    assert sub(test_list, start, end) == [2, 9, 11] 


def test_sub_end() -> None:
    """Tests the sub function's ability to create a list from values at the end of the original list."""
    test_list: list[int] = [5, 8, 2, 9, 11, 1, 16]
    start: int = 4
    end: int = 7
    assert sub(test_list, start, end) == [11, 1, 16] 


def test_sub_out_of_range() -> None:
    """Tests if the sub function returns an empty list if the interval of indexes given are out of range."""
    test_list: list[int] = [5, 8, 2, 9, 11, 1, 16]
    start: int = 10
    end: int = 16
    assert sub(test_list, start, end) == [] 