"""EX05 - Unit tests for utils functions."""

__author__ = "730309157"

from exercises.ex05.utils import only_evens, sub, concat


def test_empty() -> None:
    """Tests empty list in only_evens."""
    assert only_evens([]) == []


def test_some_evens() -> None:
    """Tests list with some even values in only_evens."""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_all_evens() -> None: 
    """Tests list with all even values in only_evens."""
    assert only_evens([2, 4, 6, 8]) == [2, 4, 6, 8]


def test_empty_lists() -> None:
    """Tests two empty lists in concat."""
    assert concat([], []) == []


def test_one_list_negative() -> None:
    """Tests one list with all negative values in concat."""
    assert concat([-3, -2, -1], [0, 1, 2, 3]) == [-3, -2, -1, 0, 1, 2, 3]


def test_positive_lists() -> None:
    """Tests two lists with all positive values in concat."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_empty_list() -> None:
    """Tests empty list in sub."""
    assert sub([], 1, 5) == []


def test_index_in_range() -> None:
    """Tests start_index and end_index within range of list in sub."""
    assert sub([1, 2, 3, 4], 0, 3) == [1, 2, 3]


def test_large_end_index() -> None:
    """Tests end_index out of range of list in sub."""
    assert sub([1, 2, 3, 4], 1, 6) == [2, 3, 4]