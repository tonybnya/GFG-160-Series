"""
Test 001. Second Largest
"""

import pytest

from gfg_001_second_largest import (get_second_largest_1, get_second_largest_2,
                                    get_second_largest_3)


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([10, 10, 10], -1),  # All elements same
        ([12, 35, 1, 10, 34, 1], 34),  # General case
        ([10, 5, 10], 5),  # Second largest smaller than repeated max
        ([5, 5], -1),  # Only two equal elements
        ([5, 6], 5),  # Simple case, two different elements
        ([1, 2, 3, 4, 5], 4),  # Increasing order
        ([5, 4, 3, 2, 1], 4),  # Decreasing order
        ([100000, 99999], 99999),  # Upper limit values
        ([2, 2, 1], 1),  # Max repeated, valid second largest
        ([1, 2, 2], 1),  # Max repeated at end
        ([2, 3, 4, 4], 3),  # Max repeated at end
        ([4, 4, 3, 2, 1], 3),  # Max repeated at start
        ([1, 2], 1),  # Two distinct elements
        ([1, 1, 2], 1),  # Max at end
        ([3, 3, 3, 2], 2),  # All but one element same
        ([1, 2, 3, 3], 2),  # Second largest not adjacent to largest
    ],
)
def test_get_second_largest_1(arr: list[int], expected: int) -> None:
    """
    Test.
    """
    assert get_second_largest_1(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([10, 10, 10], -1),  # All elements same
        ([12, 35, 1, 10, 34, 1], 34),  # General case
        ([10, 5, 10], 5),  # Second largest smaller than repeated max
        ([5, 5], -1),  # Only two equal elements
        ([5, 6], 5),  # Simple case, two different elements
        ([1, 2, 3, 4, 5], 4),  # Increasing order
        ([5, 4, 3, 2, 1], 4),  # Decreasing order
        ([100000, 99999], 99999),  # Upper limit values
        ([2, 2, 1], 1),  # Max repeated, valid second largest
        ([1, 2, 2], 1),  # Max repeated at end
        ([2, 3, 4, 4], 3),  # Max repeated at end
        ([4, 4, 3, 2, 1], 3),  # Max repeated at start
        ([1, 2], 1),  # Two distinct elements
        ([1, 1, 2], 1),  # Max at end
        ([3, 3, 3, 2], 2),  # All but one element same
        ([1, 2, 3, 3], 2),  # Second largest not adjacent to largest
    ],
)
def test_get_second_largest_2(arr: list[int], expected: int) -> None:
    """
    Test.
    """
    assert get_second_largest_2(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([10, 10, 10], -1),  # All elements same
        ([12, 35, 1, 10, 34, 1], 34),  # General case
        ([10, 5, 10], 5),  # Second largest smaller than repeated max
        ([5, 5], -1),  # Only two equal elements
        ([5, 6], 5),  # Simple case, two different elements
        ([1, 2, 3, 4, 5], 4),  # Increasing order
        ([5, 4, 3, 2, 1], 4),  # Decreasing order
        ([100000, 99999], 99999),  # Upper limit values
        ([2, 2, 1], 1),  # Max repeated, valid second largest
        ([1, 2, 2], 1),  # Max repeated at end
        ([2, 3, 4, 4], 3),  # Max repeated at end
        ([4, 4, 3, 2, 1], 3),  # Max repeated at start
        ([1, 2], 1),  # Two distinct elements
        ([1, 1, 2], 1),  # Max at end
        ([3, 3, 3, 2], 2),  # All but one element same
        ([1, 2, 3, 3], 2),  # Second largest not adjacent to largest
    ],
)
def test_get_second_largest_3(arr: list[int], expected: int) -> None:
    """
    Test.
    """
    assert get_second_largest_3(arr) == expected
