"""
You can concatenate two lists with the + operator in Python!
"""


def slice_contact(list1: list, list2: list) -> list:
    """
    Concatenate two lists with the + operator.
    """
    return list1 + list2


if __name__ == "__main__":
    slice1 = [1, 2, 3]

    print(slice_contact(slice1, [4, 5, 6]))
