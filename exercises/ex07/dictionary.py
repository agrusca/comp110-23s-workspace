"""EX07 - Dictionary functions."""

__author__ = "730309157"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Given my_dict, returns dictionary with inverted keys and values."""
    inverted_dict: dict[str, str] = dict()
    value_list: list[str] = []
    for key in my_dict:
        value_list.append(my_dict[key])
    for index in range(0, len(value_list)):
        for tracker_index in range(index + 1, len(value_list)):
            if value_list[index] == value_list[tracker_index]:
                raise KeyError("Inverting this dictionary would create duplicate keys.")
    for key in my_dict:
        inverted_dict[my_dict[key]] = key
    return inverted_dict


def favorite_color(my_dict: dict[str, str]) -> str:
    """Given my_dict, returns the value that appears most frequently."""
    counting_dict: dict[str, int] = {}
    highest_count: int = 0
    most_frequent_color: str = ""
    for key in my_dict:
        if my_dict[key] in counting_dict:
            counting_dict[my_dict[key]] += 1
        else:
            counting_dict[my_dict[key]] = 1
    for color in counting_dict:
        if counting_dict[color] > highest_count:
            highest_count = counting_dict[color]
            most_frequent_color = color
    return most_frequent_color


def count(my_list: list[str]) -> dict[str, int]:
    """Given my_list, returns a dict where each key is a unique value in my_list and the associated value is the count of the number of times that value appeared in my_list."""
    output_dict: dict[str, int] = {}
    for item in my_list: 
        if item in output_dict:
            output_dict[item] += 1
        else: 
            output_dict[item] = 1
    return output_dict