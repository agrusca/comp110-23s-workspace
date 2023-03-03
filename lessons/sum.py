"""Example function for unit tests"""

def sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total: float = 0.0
    for number in range(0, len(xs)):
        sum_total += xs[number]
    return(sum_total)

    