"""
Test 002. Move Zeroes to End
"""

import pytest

from gfg_002_move_all_zeroes_to_end import (
    move_all_zeroes_to_end_1,
    move_all_zeroes_to_end_2,
)


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 0, 4, 3, 0, 5, 0], [1, 2, 4, 3, 5, 0, 0, 0]),  # Mixed zeros
        ([10, 20, 30], [10, 20, 30]),  # No zero
        ([0, 0], [0, 0]),  # All zeros
        ([0, 1, 0, 2, 0, 3], [1, 2, 3, 0, 0, 0]),  # Alternating zeros
        ([1, 0, 2, 0, 3, 0, 4], [1, 2, 3, 4, 0, 0, 0]),  # Non-zero/zero interleaved
        ([0], [0]),  # Single element zero
        ([5], [5]),  # Single element non-zero
        ([0, 1], [1, 0]),  # Zero followed by non-zero
        ([1, 0], [1, 0]),  # Non-zero followed by zero
        ([0, 0, 0, 1], [1, 0, 0, 0]),  # Zeros followed by one non-zero
        ([1, 0, 0, 0], [1, 0, 0, 0]),  # Non-zero followed by all zeros
        ([0, 1, 0, 2, 0, 0, 3, 4], [1, 2, 3, 4, 0, 0, 0, 0]),  # Many zeros and numbers
        ([0, 100000, 0, 0, 99999], [100000, 99999, 0, 0, 0]),  # Large values
    ],
)
def test_move_all_zeroes_to_end_1(arr: list[int], expected: list[int]) -> None:
    """
    Test.
    """
    assert move_all_zeroes_to_end_1(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 0, 4, 3, 0, 5, 0], [1, 2, 4, 3, 5, 0, 0, 0]),  # Mixed zeros
        ([10, 20, 30], [10, 20, 30]),  # No zero
        ([0, 0], [0, 0]),  # All zeros
        ([0, 1, 0, 2, 0, 3], [1, 2, 3, 0, 0, 0]),  # Alternating zeros
        ([1, 0, 2, 0, 3, 0, 4], [1, 2, 3, 4, 0, 0, 0]),  # Non-zero/zero interleaved
        ([0], [0]),  # Single element zero
        ([5], [5]),  # Single element non-zero
        ([0, 1], [1, 0]),  # Zero followed by non-zero
        ([1, 0], [1, 0]),  # Non-zero followed by zero
        ([0, 0, 0, 1], [1, 0, 0, 0]),  # Zeros followed by one non-zero
        ([1, 0, 0, 0], [1, 0, 0, 0]),  # Non-zero followed by all zeros
        ([0, 1, 0, 2, 0, 0, 3, 4], [1, 2, 3, 4, 0, 0, 0, 0]),  # Many zeros and numbers
        ([0, 100000, 0, 0, 99999], [100000, 99999, 0, 0, 0]),  # Large values
    ],
)
def test_move_all_zeroes_to_end_2(arr: list[int], expected: list[int]) -> None:
    """
    Test.
    """
    assert move_all_zeroes_to_end_2(arr) == expected
