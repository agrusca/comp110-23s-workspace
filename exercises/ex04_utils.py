"""EX04 - List utility functions."""

__author__ = "730309157"


def all(int_list: list[int], single_int: int) -> bool:
    """Given int_list and single_int, returns bool indicating whether single_int is equal to every value in list_int."""
    if len(int_list) == 0:
        return False
    idx: int = 0
    while idx < len(int_list):
        if int_list[idx] != single_int:
            return False
        else:
            idx += 1
    return True


def max(input: list[int]) -> int:
    """Given input, returns the largest int in input."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    current_max: int = input[0]
    while idx < len(input):
        if input[idx] >= current_max:
            current_max = input[idx]
        idx += 1
    return current_max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given list1 and list2 of int values, returns True if every element at every index is equal in list1 and list2."""
    idx: int = 0 
    if len(list1) != len(list2):
        return False
    while idx < len(list1) and idx < len(list2):
        if list1[idx] != list2[idx]:
            return False
        else: 
            idx += 1
    return True