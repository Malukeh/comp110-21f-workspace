"""List Utility Functions."""


__author__ = "730319407"


def only_evens(list1: list[int]) -> list:
    """Returning list only containing even numbers."""
    r_list = []
    x = 0
    while x < len(list1):
        if list1[x] % 2 == 0:
            r_list.append(list1[x])
        x += 1
    return r_list


def sub(m_list: list[int], start_int: int, end_int: int) -> list:
    """Returning a sublist from the starting index to the ending index -1."""
    if start_int < 0:
        start_int = 0    
    if end_int > len(m_list):
        end_int = len(m_list)
    if len(m_list) == 0 or start_int > len(m_list) or end_int <= 0:
        return []
    r_list = []
    i = start_int
    while i < end_int:
        r_list.append(m_list[i])
        i += 1
    return r_list


def concat(list1: list[int], list2: list[int]) -> list:
    """Concatinating two lists into one."""
    r_list = []
    x = 0
    while x < len(list1):
        r_list.append(list1[x])
        x += 1
    x = 0
    while x < len(list2):
        r_list.append(list2[x])
        x += 1
    return r_list