"""Short words."""

__author__ = "730309157"


def short_words(list1: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    new_list: list[str] = list()
    for words in list1:
        if len(words) < 5:
            new_list.append(words)
        else:
            print(f"{words} is too long!")
    return new_list