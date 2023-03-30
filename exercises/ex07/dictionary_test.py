"""Dictionary Function Test - EX07!"""

__author__ = "730575328"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_use() -> None:
    """Use case test for invert function."""
    dict_list: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(dict_list) == {"b": "a", "d": "c", "f": "e"}


def test_invert_use2() -> None:
    """Second use case test for invert function."""
    dict_list: dict[str, str] = {"cat": "dog"}
    assert invert(dict_list) == {"dog": "cat"}


def test_invert_edge() -> None:
    """Edge test for invert function."""
    dict_list: dict[str, str] = {}
    assert invert(dict_list) == {}


def test_favorite_color_use() -> None:
    """Use case test for the favorite color function for a tie."""
    dict_list: dict[str, str] = {"max": "brown", "matt": "green", "julian": "brown", "jasper": "green"}
    assert favorite_color(dict_list) == {"brown"}


def test_favorite_color_use2() -> None:
    """Second use case test for the favorite color function."""
    dict_list: dict[str, str] = {"maddi": "lavender", "lucy": "red", "aarya": "blue", "jude bellingham": "lavender"}
    assert favorite_color(dict_list) == {"lavender"}


def test_favorite_color_edge() -> None:
    """Edge case test for the favorite color function."""
    dict_list: dict[str, str] = {}
    assert favorite_color(dict_list) == {}


def test_count_use() -> None:
    """Use case test for the count function."""
    test_list: list[str] = ["apple", "apple", "orange", "apple", "grapes"]
    assert count(test_list) == {'apple': 3, 'orange': 1, 'grapes': 1}


def test_count_use2() -> None:
    """Second use case test for the count function."""
    test_list: list[str] = ["fish", "shark", "shark", "orca", "orca"]
    assert count(test_list) == {'fish': 1, 'shark': 2, 'orca': 2}


def test_count_edge() -> None:
    """Edge case test for the count function."""
    test_list: list[str] = []
    assert count(test_list) == {}