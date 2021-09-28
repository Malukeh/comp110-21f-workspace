"""List utility functions."""

__author__ = "730319407"

# TODO: Implement your functions here.


def all(main_list: 'list[int]', i: int) -> bool:
    while len(main_list) > 0:
        if i == main_list.pop(0):
            return True
    return False


def is_equal(list1: 'list[int]', list2: 'list[int]') -> bool:
    while len(list1) > 0:
        if list1.pop(0) != list2.pop(0):
            return False
    return True


def max(input: 'list[int]') -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_int = input.pop(0)
    while len(input) > 0:
        if max_int < input[0]:
            max_int = input.pop(0)
        else:
            input.pop(0)
    return max_int