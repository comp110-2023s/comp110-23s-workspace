"""EX07 - Dictionary Test Functions."""

__author__ = "730556365"


from exercises.ex07.dictionary import invert, favorite_color, count

def test_invert_city_state() -> None:
    """Tests the invert function when states are the keys and cities are the values of an inputed dictionary."""
    test_dict: dict[str, str] = {"North Carolina": "Chapel Hill", "Florida": "Miami", "Georgia": "Atlanta"}
    assert invert(test_dict) == {"Chapel Hill": "North Carolina", "Miami": "Florida", "Atlanta": "Georgia"}

def test_invert_student_score() -> None:
    """Tests the invert function when test scores are the keys and student names are the values of an inputed dictionary."""
    test_dict: dict[str, str] = {"98": "Alicia", "82": "Devin", "75": "Jason"}
    assert invert(test_dict) == {"Alicia": "98", "Devin": "82", "Jason": "75"}


def test_invert_empty() -> None:
    """Tests the invert function when the inputed dictionary is empty."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_favorite_color_tie() -> None:
    """Tests the favorite_color function when there are multiple colors tied for most appearances."""
    test_dict: dict[str, str] = {"Sebastian": "red", "Ana": "blue", "Carter": "blue", "Anthony": "red"}
    assert favorite_color(test_dict) == "red"


def test_favorite_color_different() -> None:
    """Tests the favorite_color function when there are a different number of appearances for each color/"""
    test_dict: dict[str, str] = {"Sara": "red", "Jackson": "blue", "Martin": "blue", "Taylor": "purple"}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_empty() -> None:
    """Tests the favorite_color function when the inputed dictionary is empty."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_count_one_instance() -> None:
    """Tests the count function when there is only one instance of each item."""
    test_list: list[str] = ["donut", "cookie", "cake", "ice cream"]
    assert count(test_list) == {"donut": 1, "cookie": 1, "cake": 1, "ice cream": 1}


def test_count_multiple_instances() -> None:
    """Tests the count function when there are multiple instances of each item."""
    test_list: list[str] = ["waffle", "waffle", "pancake", "waffle", "pancake"]
    assert count(test_list) == {"waffle": 3, "pancake": 2}


def test_count_empty() -> None:
    """Tests the count function when the inputed list is empty."""
    test_list: list[str] = []
    assert count(test_list) == {}