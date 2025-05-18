"""
Test 006. Majority Element II
"""

import pytest

from gfg_006_majority_element_II import find_majority_1, find_majority_2


@pytest.mark.parametrize(
    "arr, expected",
    [
        # Two elements appear more than n/3 times
        ([2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6], [5, 6]),
        # No element appears more than n/3 times
        ([1, 2, 3, 4, 5], []),
        # One majority element
        ([1, 1, 1, 2, 3], [1]),
        # All elements are the same
        ([4, 4, 4, 4], [4]),
        # Two elements exactly meet the threshold
        ([3, 3, 3, 4, 4, 4, 5], [3, 4]),
        # Large input, all unique
        (list(range(1, 100001)), []),
        # One negative majority
        ([-1, -1, -1, 2], [-1]),
        # Elements at the threshold but not above
        ([7, 7, 8, 8, 9, 9], []),
        # Two elements just above the threshold
        ([10, 10, 10, 20, 20, 20, 30], [10, 20]),
        # Single element
        ([1], [1]),
    ],
)
def test_find_majority_1(arr: list[int], expected: list[int]) -> None:
    """
    Test.
    """
    assert find_majority_1(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        # Two elements appear more than n/3 times
        ([2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6], [5, 6]),
        # No element appears more than n/3 times
        ([1, 2, 3, 4, 5], []),
        # One majority element
        ([1, 1, 1, 2, 3], [1]),
        # All elements are the same
        ([4, 4, 4, 4], [4]),
        # Two elements exactly meet the threshold
        ([3, 3, 3, 4, 4, 4, 5], [3, 4]),
        # Large input, all unique
        (list(range(1, 100001)), []),
        # One negative majority
        ([-1, -1, -1, 2], [-1]),
        # Elements at the threshold but not above
        ([7, 7, 8, 8, 9, 9], []),
        # Two elements just above the threshold
        ([10, 10, 10, 20, 20, 20, 30], [10, 20]),
        # Single element
        ([1], [1]),
    ],
)
def test_find_majority_2(arr: list[int], expected: list[int]) -> None:
    """
    Test.
    """
    assert find_majority_2(arr) == expected
