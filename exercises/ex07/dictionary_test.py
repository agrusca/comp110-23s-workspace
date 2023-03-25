"""EX07 - Dictionary functions unit tests."""

__author__ = "730309157"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_empty_dict() -> None:
    """Tests empty input dictionary in invert."""
    assert invert({}) == {}


def test_small_dict() -> None:
    """Tests small input dictionary in invert."""
    assert invert({"apple": "fruit", "eggplant": "vegetable"}) == {"fruit": "apple", "vegetable": "eggplant"}


def test_large_dict() -> None:
    """Tests large input dictionary in invert."""
    assert invert({"calculus": "math", "biology": "science", "history": "social studies", "english": "language", "yoga": "physical education"}) == {"math": "calculus", "science": "biology", "social studies": "history", "language": "english", "physical education": "yoga"}


def test_empty_color_dict() -> None:
    """Tests empty input dictionary in favorite_color."""
    assert favorite_color({}) == ""


def test_uniqe_favorite_color() -> None:
    """Tests input dictionary where one value shows up most frequently in favorite_color."""
    assert favorite_color({"Alexa": "blue", "John": "blue", "Baylee": "yellow", "Hank": "green"}) == "blue"


def test_several_favorite_colors() -> None:
    """Tests input dictionary where more than one value shows up most frequently in favorite_color."""
    assert favorite_color({"Alexa": "blue", "John": "blue", "Baylee": "yellow", "Hank": "yellow"}) == "blue"


def test_empty_list() -> None:
    """Tets empty input list in count."""
    assert count([]) == {}


def test_unique_list() -> None:
    """Tests input list with unique values."""
    assert count(["apple", "orange", "banana", "strawberry"]) == {"apple": 1, "orange": 1, "banana": 1, "strawberry": 1}


def test_redundant_list() -> None: 
    """Tests input list with redundant values."""
    assert count(["apple", "apple", "banana", "banana"]) == {"apple": 2, "banana": 2}


