"""
Test 009. Minimize the Heights II
"""

import pytest

from gfg_009_minimize_the_heights_II import get_min_diff_1


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        # Format: ((arr, k), expected)
        # Test Case 1: Example from prompt
        ([1, 5, 8, 10], 2, 5),
        # Test Case 2: Another prompt example
        ([3, 9, 12, 16, 20], 3, 11),
        # Test Case 3: All elements same
        ([7, 7, 7, 7], 5, 0),
        # Test Case 5: Large K, avoid negatives
        ([1, 2, 3], 100, 2),  # only increasing is safe → [101, 102, 103]
        # Test Case 10: Single element
        ([100], 5, 0),
    ],
)
def test_get_min_diff_1(arr: list[int], k: int, expected: int) -> None:
    """
    Test.
    """
    assert get_min_diff_1(arr, k) == expected
