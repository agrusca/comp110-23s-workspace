"""Odd and even function."""

def odd_and_even(int_list: list[int]) -> list[int]:
    """Test"""
    new_list: list[int] = list()
    for idx in range(0, len(int_list)):
        if idx % 2 == 0 and int_list[idx] % 2 != 0:
            new_list.append(int_list[idx])
    return new_list

print(odd_and_even([7, 8 , 10, 10, 5, 12, 3, 2, 11, 8]))
