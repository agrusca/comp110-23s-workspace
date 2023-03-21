"""Value exists function."""

def value_exists(dict1: dict[str, int], int1: int) -> bool:
    """Test"""
    for item in dict1: 
        if dict1[item] == int1:
            return True
    return False
            

