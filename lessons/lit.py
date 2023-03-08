"""untit test for untils"""

from exercises.ex05.utils import only_evens

def test1() -> None:
    test_list: list[int] = ([1, 2, 3])
    assert only_evens(test_list) == 2

def test2() -> None:
    test_list: list[int] = ([1, 5, 3])
    assert only_evens(test_list) == []

def test3() -> None:
    test_list: list[int] = ([4, 4, 4])
    assert only_evens(test_list) == [4, 4, 4]
