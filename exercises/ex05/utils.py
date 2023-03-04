"""EX05 - List utility functions, continued."""

__author__ = "730309157"


def only_evens(int_list: list[int]) -> list[int]:
    """Given an int_list, returns new list contanining only even elements of int_list."""
    even_list: list[int] = list()
    for number in int_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Given list_1 and list_2, returns all elements of list_1, followed by all elements of list_2."""
    concat_list: list[int] = list()
    for number in list_1:
        concat_list.append(number)
    for number in list_2:
        concat_list.append(number)
    return concat_list


def sub(list_1: list[int], start_index: int, end_index: int) -> list[int]:
    """Given list_1, start_index, and end_index, generates list which is a subset of list_1, between start_index and end_index - 1."""
    subset_list: list[int] = list()
    if start_index < 0:
        for idx in range(0, end_index):
            subset_list.append(list_1[idx])
        return subset_list
    if end_index > len(list_1):
        for idx in range(start_index, len(list_1)):
            subset_list.append(list_1[idx])
        return subset_list
    if len(list_1) == 0 or start_index >= len(list_1) or end_index <= 0:
        return subset_list
    for idx in range(start_index, end_index):
        subset_list.append(list_1[idx])
    return subset_list