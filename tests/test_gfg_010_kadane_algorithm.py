"""
Test 010. Kadane's Algorithm
"""

import pytest

from gfg_010_kadane_algorithm import max_subarray_sum_1, max_subarray_sum_2


@pytest.mark.parametrize(
    "arr, expected",
    [
        # Format: (arr, expected)

        # Test Case 1: From the prompt
        ([2, 3, -8, 7, -1, 2, 3], 11),

        # Test Case 2: All negative elements
        ([-2, -4], -2),

        # Test Case 3: All positive elements
        ([5, 4, 1, 7, 8], 25),

        # Test Case 4: Mix of negatives and positives
        ([1, -2, 3, 4, -1, 2, 1, -5, 4], 9),

        # Test Case 5: Single element (positive)
        ([7], 7),

        # Test Case 6: Single element (negative)
        ([-3], -3),

        # Test Case 7: Large negative dip
        ([4, -1, 2, 1, -7, 5, 6], 11),

        # Test Case 8: All elements zero
        ([0, 0, 0, 0], 0),

        # Test Case 9: Leading and trailing negatives
        ([-5, 1, 2, 3, -2, 4, -1], 8),

        # Test Case 10: Long negative prefix before subarray
        ([-10, -5, 2, 3, -1, 2, -1, 4], 9),
    ],
)
def test_max_subarray_sum_1(arr: list[int], expected: int) -> None:
    """
    Test.
    """
    assert max_subarray_sum_1(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        # Format: (arr, expected)

        # Test Case 1: From the prompt
        ([2, 3, -8, 7, -1, 2, 3], 11),

        # Test Case 2: All negative elements
        ([-2, -4], -2),

        # Test Case 3: All positive elements
        ([5, 4, 1, 7, 8], 25),

        # Test Case 4: Mix of negatives and positives
        ([1, -2, 3, 4, -1, 2, 1, -5, 4], 9),

        # Test Case 5: Single element (positive)
        ([7], 7),

        # Test Case 6: Single element (negative)
        ([-3], -3),

        # Test Case 7: Large negative dip
        ([4, -1, 2, 1, -7, 5, 6], 11),

        # Test Case 8: All elements zero
        ([0, 0, 0, 0], 0),

        # Test Case 9: Leading and trailing negatives
        ([-5, 1, 2, 3, -2, 4, -1], 8),

        # Test Case 10: Long negative prefix before subarray
        ([-10, -5, 2, 3, -1, 2, -1, 4], 9),
    ],
)
def test_max_subarray_sum_2(arr: list[int], expected: int) -> None:
    """
    Test.
    """
    assert max_subarray_sum_2(arr) == expected
