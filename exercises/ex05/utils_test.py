"""Testing List Utility Functions."""


__author__ = "730319407"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Testing edge case for only_evens."""
    list1: list[int] = []
    assert only_evens(list1) == []


def test_only_evens_single_item() -> None:
    """Testing single item for only_evens."""
    list1: list[int] = [110]
    assert only_evens(list1) == [110]


def test_only_evens_many_items() -> None:
    """Testing many items for only_evens."""
    list1: list[int] = [1, 2, 3]
    assert only_evens(list1) == [2]


def test_sub_empty() -> None:
    """Testing edge case for sub."""
    list1: list[int] = []
    assert sub(list1, 0, 0) == []


def test_sub_single_item() -> None:
    """Testing single item for sub."""
    list1: list[int] = [110]
    assert sub(list1, 0, 1) == [110]


def test_sub_many_items() -> None:
    """Testing many items for sub."""
    list1: list[int] = [1, 2, 3]
    assert sub(list1, 1, 3) == [2, 3]


def test_concat_empty() -> None:
    """Testing edge case for concat."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def test_concat_single_item() -> None:
    """Testing single item for concat."""
    list1: list[int] = [110]
    list2: list[int] = [15]
    assert concat(list1, list2) == [110, 15]


def test_concat_many_items() -> None:
    """Testing many items for concat."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6]