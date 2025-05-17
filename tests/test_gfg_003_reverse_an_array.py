"""
Test 003. Reverse an Array
"""

import pytest

from gfg_003_reverse_an_array import reverse_an_array_1, reverse_an_array_2


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 4, 3, 2, 6, 5], [5, 6, 2, 3, 4, 1]),  # Even number of elements
        ([4, 5, 2], [2, 5, 4]),  # Odd number of elements
        ([1], [1]),  # Single element
        ([2, 1], [1, 2]),  # Two elements
        ([10, 20, 30, 40], [40, 30, 20, 10]),  # Simple case
        ([5, 5, 5, 5], [5, 5, 5, 5]),  # All elements the same
        ([0, 0, 1], [1, 0, 0]),  # With zeroes
        ([100000, 0, 99999], [99999, 0, 100000]),  # Extreme values
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),  # Already in increasing order
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Already in decreasing order
    ],
)
def test_reverse_an_array_1(arr: list[int], expected: list[int]) -> None:
    """
    Test.
    """
    assert reverse_an_array_1(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 4, 3, 2, 6, 5], [5, 6, 2, 3, 4, 1]),  # Even number of elements
        ([4, 5, 2], [2, 5, 4]),  # Odd number of elements
        ([1], [1]),  # Single element
        ([2, 1], [1, 2]),  # Two elements
        ([10, 20, 30, 40], [40, 30, 20, 10]),  # Simple case
        ([5, 5, 5, 5], [5, 5, 5, 5]),  # All elements the same
        ([0, 0, 1], [1, 0, 0]),  # With zeroes
        ([100000, 0, 99999], [99999, 0, 100000]),  # Extreme values
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),  # Already in increasing order
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Already in decreasing order
    ],
)
def test_reverse_an_array_2(arr: list[int], expected: list[int]) -> None:
    """
    Test.
    """
    assert reverse_an_array_2(arr) == expected
