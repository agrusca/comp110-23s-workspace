"""Dict function writing"""

def zip(str_list: list[str], int_list:list[int]) -> dict[str, int]:
    """Returns dictionary with key of str_list and values of int_list at same index."""
    if len(str_list) != len(int_list) or len(str_list) == 0 or len(int_list) == 0:
        return {}
    final_dict: dict = {}
    for number in range(0, len(str_list)):
        final_dict[str_list[number]] = int_list[number]
    return final_dict